import glob
import os
import sys
from pydriller import GitRepository, RepositoryMining, domain
import csv
import json
import math
import statistics
from tqdm import tqdm

import datetime
import re

class Dataset:
    def __init__(self, repositories):
        self.dataset=[]
        self.repositories=repositories
    def prepare(self):
        for repository in self.repositories:
            datasetRepository=[]
            if(not os.path.exists(repository["path"])):
                pass
                #rawdata=Rawdata()
            gr = GitRepository(repository["path"])
            pathsFile = [pathFile for pathFile in glob.glob(repository["path"]+"/**/*.mjava", recursive=True) if re.match(repository["filterFile"], pathFile)]
            commitsBug=self.getCommitsBug(repository)

            with tqdm(pathsFile,bar_format="{desc}: {percentage:3.0f}%|{bar:10}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}{postfix}]") as pbar:
                for pathFile in pbar:
                    nameFile=os.path.basename(pathFile)
                    pbar.postfix=nameFile
                    pbar.desc=repository["name"]
                    datasetRepository.append(Data(gr, pathFile, commitsBug).getData())
            self.dataset.extend(datasetRepository)
    def getCommitsBug(self, repository):
        commitsBug={}
        annotations=json.load(open(repository["pathAnnotations"], 'r'))
        for commit in annotations:
            for i in range(len(annotations[commit])):
                if(not commit in commitsBug):
                    commitsBug[commit]={"fix":[], "prefix":[], "intro":[]} # prefix を追加
                commitsBug[commit]["fix"].append(annotations[commit][i]["filePath"])
                for revision in annotations[commit][i]["revisions"]:
                    if(revision!=commit):
                        if(not revision in commitsBug):
                             commitsBug[revision]={"fix":[], "prefix":[], "intro":[]}
                        commitsBug[revision]["intro"].append(annotations[commit][i]["filePath"])
        return commitsBug
    def save(self, path):
        with open(path, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.dataset)
    def load(self):
        pass
    def visualize(self):
        pass
class Data:
    def __init__(self, gr, pathFile, commitsBug):
        self.gr=gr
        self.pathFile=pathFile
        self.nameFile=os.path.basename(pathFile)
        self.commits=[]
        commits=self.gr.get_commits_modified_file(self.pathFile)
        print("-----------------------------------------------")
        print(pathFile)
        #print("all commits")
        #print(commits)
        pathTmp=pathFile
        with open("log", mode='a') as f:
            for commit in commits:
                for modification in self.gr.get_commit(commit).modifications:
                    if (pathTmp == modification.new_path):
                        if (modification.change_type==modification.change_type.MODIFY) or (modification.change_type==modification.change_type.ADD):
                            print(commit)
                            print(modification.change_type)
                            print(modification.old_path)
                            self.commits.append(commit)
                            #if modification.change_type==modification.change_type.ADD:
                            #    break
                        pathTmp=modification.old_path
        #print("selected commits")
        print("commits: "+str(len(self.commits)))
        self.commitsBug=commitsBug
    def getData(self):
        return [
            self.calculateLOC(),
        ]
    def calculateLOC(self):
        LOC=0
        with open(self.pathFile, "r") as fr:
            lines=fr.read().splitlines()
            for i, line in enumerate(lines):
                #patternLineIgnore="^(\s*{\s*|\s*|\s*//.*|\s*case.*)$"
                patternLineIgnore="^(\s*|\s*//.*)$"
                if re.match(patternLineIgnore,line):
                    continue
                LOC=LOC+1
        return LOC
    def calculateLOCtest(self):
        LOC=0
        with open(self.pathFile, "r") as fr:
            lines=fr.read().splitlines()
            for i, line in enumerate(lines):
                #patternLineIgnore="^(\s*{\s*|\s*|\s*//.*|\s*case.*)$"
                patternLineIgnore="^(\s*|\s*//.*)$"
                if re.match(patternLineIgnore,line):
                    continue
                LOC=LOC+1
        return LOC
    def calculateLOCtest0(self):
        LOC=0
        with open(self.pathFile, "r") as fr:
            lines=fr.read().splitlines()
            for i, line in enumerate(lines):
                #patternLineIgnore="^(\s*{\s*|\s*|\s*//.*|\s*case.*)$"
                patternLineIgnore="^(\s*|\s*//.*)$"
                if re.match(patternLineIgnore,line):
                    continue
                LOC=LOC+1
        return LOC        