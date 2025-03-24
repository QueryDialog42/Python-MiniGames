from sys import stdin, stderr
from typing import Any
from string import digits, ascii_letters
from colorama import Fore
import datetime
def createtable(*args: list | str, space: int, title: bool = False, format: int = 1, export:str = None, foot:str = None, nullentity:str = "__NULL__",
                 leftbodyborder:str = "|", rightbodyborder:str = "|", lefttitleborder:str = "|", righttitleborder:str = "|",
                   topborder:str = "=", middleborder:str = "=", underborder:str = "=", head:str = None, leftheadborder:str = "|", rightheadborder:str = "|",
                   leftfootborder:str = "|", rightfootborder:str = "|") -> None:
    class TableNeeds:
        @staticmethod
        def findlongestlist() -> int:
            longestlist = 0
            for lists in args:
                if len(lists) > longestlist:
                    longestlist = len(lists)
                else: continue
            return longestlist
        @staticmethod
        def listobjectlongs(sumobjectlen:str, strlists:list, i:int) -> None:
            if i < len(strlists):
                sumobjectlen += strlists[i] + " " * (space - len(strlists[i]))
            else:
                sumobjectlen += nullentity + " " * (space - len(nullentity))
            return sumobjectlen
        @staticmethod
        def listobjectcompiler(sumobjectlen, strlists, i) -> int:
            if i < len(strlists):
                sumobjectlen = len(sumobjectlen.removesuffix(" " * (space - len(strlists[i]))))
            else:
                sumobjectlen = len(sumobjectlen.removesuffix(" " * (space - len(nullentity))))
            return sumobjectlen
        @staticmethod
        def findlongestlistobjectformat1(longestlist) -> int:
            longestlistobjectformat1 = 0
            for lists in args:
                strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                sumobjectlen = ""
                for i in range(longestlist):
                    sumobjectlen = TableNeeds.listobjectlongs(sumobjectlen, strlists, i)
                sumobjectlen = TableNeeds.listobjectcompiler(sumobjectlen, strlists, i)
                if sumobjectlen > longestlistobjectformat1:
                    longestlistobjectformat1 = sumobjectlen
                else:continue
            return longestlistobjectformat1
        @staticmethod
        def findlongestlistobjectformat2(longestlist) -> int:
            longestlistobjectformat2 = 0
            for i in range(longestlist):
                sumobjectlen = ""
                for lists in args:
                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                    sumobjectlen = TableNeeds.listobjectlongs(sumobjectlen, strlists, i)
                sumobjectlen = TableNeeds.listobjectcompiler(sumobjectlen, strlists, i)
                if sumobjectlen > longestlistobjectformat2:
                    longestlistobjectformat2 = sumobjectlen
                else:continue
            return longestlistobjectformat2
    class TablePatterns:
        @staticmethod
        def tablepattern1(strlists, longestlist, i, longestlistobjectformat1, listlong, titled = True):
            if i < len(strlists):
                if i != longestlist - 1:
                    print(strlists[i] + " " * (space - len(strlists[i])), end="", flush=True)
                    listlong += len(strlists[i] + " " * (space - len(strlists[i])))
                    return listlong
                else:
                    print(strlists[i], end="", flush=True)
                    listlong += len(strlists[i])
                    print(" " * (longestlistobjectformat1 - listlong), end=f" {rightbodyborder}", flush=True) if titled == True else print(" " * (longestlistobjectformat1 - listlong), end=f" {righttitleborder}", flush=True)
                    return listlong
            else:
                if i != longestlist - 1:
                    print(nullentity + " " * (space - len(nullentity)), end="", flush=True)
                    listlong += len(nullentity + " " * (space - len(nullentity)))
                    return listlong
                else:
                    print(nullentity, end="", flush=True)
                    listlong += len(nullentity)
                    print(" " * (longestlistobjectformat1 - listlong), end=f" {rightbodyborder}", flush=True) if titled == True else print(" " * (longestlistobjectformat1 - listlong), end=f" {righttitleborder}", flush=True)
                    return listlong
        @staticmethod
        def tablepattern2(strlists, i, longestlistobjectformat2, listlong, listnumber, titled = True) -> Any:
            if i < len(strlists):
                if listnumber != len(args):
                    print(strlists[i] + " " * (space - len(strlists[i])), end="", flush=True)
                    listlong += len(strlists[i] + " " * (space - len(strlists[i])))
                    listnumber += 1
                    yield listnumber
                    yield listlong
                else:
                    print(strlists[i], end="", flush=True)
                    listlong += len(strlists[i])
                    print(" " * (longestlistobjectformat2 - listlong), end=f" {rightbodyborder}", flush=True) if titled == True else print(" " * (longestlistobjectformat2 - listlong), end=f" {righttitleborder}", flush=True)
                    yield listnumber
                    yield listlong
            else:
                if listnumber != len(args):
                    print(nullentity + " " * (space - len(nullentity)), end="", flush=True)
                    listlong += len(nullentity + " " * (space - len(nullentity)))
                    listnumber += 1
                    yield listnumber
                    yield listlong
                else:
                    print(nullentity, end="", flush=True)
                    listlong += len(nullentity)
                    print(" " * (longestlistobjectformat2 - listlong), end=f" {rightbodyborder}", flush=True) if titled == True else print(" " * (longestlistobjectformat2 - listlong), end=f" {righttitleborder}", flush=True)
                    yield listnumber
                    yield listlong
    class TableFormatsNoTitle:
        @staticmethod
        def printtableformat1(longestlist, longestlistobjectformat1) -> None:
            if head != None:
                print(topborder * (longestlistobjectformat1 + 2 + len(leftheadborder) + len(rightheadborder)), flush=True)
                print(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else print(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder, flush=True)
            print(topborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
            for lists in args:
                strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                print(f"\n{leftbodyborder} ", end="", flush=True)
                listlong = 0
                for i in range(longestlist):
                   listlong = TablePatterns.tablepattern1(strlists, longestlist, i, longestlistobjectformat1, listlong)
            print(flush=True)
            print(underborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)), flush=True)
            if foot != None:
                print()
                print(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder) if len(foot) % 2 == 0 else print(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder, flush=True)
                print(underborder * (longestlistobjectformat1 + 2 + len(leftfootborder) + len(rightfootborder)), flush=True)
        @staticmethod
        def printtableformat2(longestlist, longestlistobjectformat2) -> None:
            if head != None:
                print(topborder * (longestlistobjectformat2 + 2 + len(leftheadborder) + len(rightheadborder)), flush=True)
                print(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else print(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder, flush=True)
            print(topborder * (longestlistobjectformat2 + 2 + len(leftheadborder) + len(rightheadborder)), end="", flush=True)
            for i in range(longestlist):
                print(f"\n{leftbodyborder} ", end="", flush=True)
                listlong = 0
                listnumber = 1
                for lists in args:
                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                    values = TablePatterns.tablepattern2(strlists, i, longestlistobjectformat2, listlong, listnumber)
                    listnumber = next(values)
                    listlong = next(values)
            print(flush=True)
            print(underborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
            if foot != None:
                print()
                print(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder) if len(foot) % 2 == 0 else print(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder, flush=True)
                print(underborder * (longestlistobjectformat2 + 2 + len(leftfootborder) + len(rightfootborder)), flush=True)
    class TableFormatWithTitle:
        @staticmethod
        def printtableformat1(longestlist, longestlistobjectformat1) -> None:
            titled = False
            if head != None:
                print()
                print(topborder * (longestlistobjectformat1 + 2 + len(leftheadborder) + len(rightheadborder)), flush=True)
                print(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else print(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
            print(topborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
            for lists in args:
                strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                print(f"\n{leftbodyborder} ", end="", flush=True) if titled == True else print(f"\n{lefttitleborder} ", end="", flush=True)
                listlong = 0
                for i in range(longestlist):
                    listlong = TablePatterns.tablepattern1(strlists, longestlist, i, longestlistobjectformat1, listlong, titled)
                if titled == False:
                    print(flush=True)
                    print(middleborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
                    titled = True
            print(flush=True)
            print(underborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)), flush=True)
            if foot != None:
                print(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder) if len(foot) % 2 == 0 else print(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder, flush=True)
                print(underborder * (longestlistobjectformat1 + 2 + len(leftfootborder) + len(rightfootborder)), flush=True)
        @staticmethod
        def printtableformat2(longestlist, longestlistobjectformat2) -> None:
            titled = False
            if head != None:
                print()
                print(topborder * (longestlistobjectformat2 + 2 + len(leftheadborder) + len(rightheadborder)), flush=True)
                print(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else print(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
            print(topborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
            for i in range(longestlist):
                print(f"\n{leftbodyborder} ", end="", flush=True) if titled == True else print(f"\n{lefttitleborder} ", end="", flush=True)
                listlong = 0
                listnumber = 1
                for lists in args:
                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                    values = TablePatterns.tablepattern2(strlists, i, longestlistobjectformat2, listlong, listnumber, titled)
                    listnumber = next(values)
                    listlong = next(values)
                if titled == False:
                    print(flush=True)
                    print(middleborder * (longestlistobjectformat2 + 2 + len(lefttitleborder) + len(righttitleborder)), end="", flush=True)
                    titled = True
            print(flush=True)
            print(underborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)), end="", flush=True)
            if foot != None:
                print()
                print(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder) if len(foot) % 2 == 0 else print(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder, flush=True)
                print(underborder * (longestlistobjectformat2 + 2 + len(leftfootborder) + len(rightfootborder)), flush=True)
    class ExportTable:
            class TablePatternsExport:
                    @staticmethod
                    def tablepattern1export(strlists, longestlist, i, longestlistobjectformat1, listlong, titled = True):
                        try:
                            if i < len(strlists):
                                if i != longestlist - 1:
                                    with open(f"{export}", "a") as file:
                                        file.write(strlists[i] + " " * (space - len(strlists[i])))
                                        listlong += len(strlists[i] + " " * (space - len(strlists[i])))
                                        return listlong
                                else:
                                    with open(f"{export}", "a") as file:
                                        file.write(strlists[i])
                                        listlong += len(strlists[i])
                                        file.write(" " * (longestlistobjectformat1 - listlong) + f" {rightbodyborder}") if titled else file.write(" " * (longestlistobjectformat1 - listlong) + f" {righttitleborder}")
                                        return listlong
                            else:
                                if i != longestlist - 1:
                                    with open(f"{export}", "a") as file:
                                        file.write(nullentity + " " * (space - len(nullentity)))
                                        listlong += len(nullentity + " " * (space - len(nullentity)))
                                        return listlong
                                else:
                                    with open(f"{export}", "a") as file:
                                        file.write(nullentity)
                                        listlong += len(nullentity)
                                        file.write(" " * (longestlistobjectformat1 - listlong) + f" {rightbodyborder}") if titled else file.write(" " * (longestlistobjectformat1 - listlong) + f" {righttitleborder}")
                                        return listlong
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
                    @staticmethod
                    def tablepattern2export(strlists, i, longestlistobjectformat2, listlong, listnumber, titled = True) -> Any:
                        try:
                            if i < len(strlists):
                                if listnumber != len(args):
                                    with open(f"{export}", "a") as file:
                                        file.write(strlists[i] + " " * (space - len(strlists[i])))
                                    listlong += len(strlists[i] + " " * (space - len(strlists[i])))
                                    listnumber += 1
                                    yield listnumber
                                    yield listlong
                                else:
                                    with open(f"{export}", "a") as file:
                                        file.write(strlists[i])
                                        listlong += len(strlists[i])
                                        file.write(" " * (longestlistobjectformat2 - listlong) + f" {rightbodyborder}") if titled else file.write(" " * (longestlistobjectformat2 - listlong) + f" {righttitleborder}")
                                    yield listnumber
                                    yield listlong
                            else:
                                if listnumber != len(args):
                                    with open(f"{export}", "a") as file:
                                        file.write(nullentity + " " * (space - len(nullentity)))
                                    listlong += len(nullentity + " " * (space - len(nullentity)))
                                    listnumber += 1
                                    yield listnumber
                                    yield listlong
                                else:
                                    with open(f"{export}", "a") as file:
                                        file.write(nullentity)
                                        listlong += len(nullentity)
                                        file.write(" " * (longestlistobjectformat2 - listlong) + f" {rightbodyborder}") if titled else file.write(" " * (longestlistobjectformat2 - listlong) + f" {righttitleborder}")
                                    yield listnumber
                                    yield listlong
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
            class ExportTableNoTitle:
                    @staticmethod
                    def exporttableformat1(longestlist, longestlistobjectformat1) -> None:
                        try:
                            if head != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n" + topborder * (longestlistobjectformat1 + 2 + len(leftheadborder) + len(rightheadborder)) + "\n")
                                    file.write(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else file.write(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
                            with open(f"{export}", "a") as file:
                                file.write("\n" + topborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            for lists in args:
                                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                                    with open(f"{export}", "a") as file:
                                        file.write(f"\n{leftbodyborder} ")
                                    listlong = 0
                                    for i in range(longestlist):
                                        listlong = ExportTable.TablePatternsExport.tablepattern1export(strlists, longestlist, i, longestlistobjectformat1, listlong)
                            with open(f"{export}", "a") as file:
                                file.write("\n" + underborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            if foot != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n")
                                    file.write(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n") if len(foot) % 2 == 0 else file.write(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n")
                                    file.write(underborder * (longestlistobjectformat1 + 2 + len(leftfootborder) + len(rightfootborder)) + "\n")
                            print(Fore.GREEN + f"The table has been created at '{export}' file | {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
                    @staticmethod
                    def exporttableformat2(longestlist, longestlistobjectformat2) -> None:
                        try:
                            if head != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n" + topborder * (longestlistobjectformat2 + 2 + len(leftheadborder) + len(rightheadborder)) + "\n")
                                    file.write(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else file.write(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
                            with open(f"{export}", "a") as file:
                                file.write("\n" + topborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            for i in range(longestlist):
                                with open(f"{export}", "a") as file:
                                    file.write(f"\n{leftbodyborder} ")
                                listlong = 0
                                listnumber = 1
                                for lists in args:
                                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                                    values = ExportTable.TablePatternsExport.tablepattern2export(strlists, i, longestlistobjectformat2, listlong, listnumber)
                                    listnumber = next(values)
                                    listlong = next(values)
                            with open(f"{export}", "a") as file:
                                file.write("\n")
                                file.write(underborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            if foot != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n")
                                    file.write(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n") if len(foot) % 2 == 0 else file.write(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n")
                                    file.write(underborder * (longestlistobjectformat2 + 2 + len(leftfootborder) + len(rightfootborder)) + "\n")
                            print(Fore.GREEN + f"The table has been created at '{export}' file | {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
            class ExportTableWithTitle:
                    @staticmethod
                    def exporttableformat1(longestlist, longestlistobjectformat1) -> None:
                        try:
                            titled = False
                            if head != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n" + topborder * (longestlistobjectformat1 + 2 + len(leftheadborder) + len(rightheadborder)) + "\n")
                                    file.write(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else file.write(leftheadborder + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat1 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
                            with open(f"{export}", "a") as file:
                                file.write("\n" + topborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            for lists in args:
                                strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                                with open(f"{export}", "a") as file:
                                    file.write(f"\n{leftbodyborder} ")
                                listlong = 0
                                for i in range(longestlist):
                                    listlong = ExportTable.TablePatternsExport.tablepattern1export(strlists, longestlist, i, longestlistobjectformat1, listlong)
                                if titled == False:
                                    with open(f"{export}", "a") as file:
                                        file.write("\n")
                                        file.write(middleborder * (longestlistobjectformat1 + 2 + len(lefttitleborder) + len(righttitleborder)))
                                    titled = True
                            with open(f"{export}", "a") as file:
                                file.write("\n")
                                file.write(underborder * (longestlistobjectformat1 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            if foot != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n")
                                    file.write(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n") if len(foot) % 2 == 0 else file.write(leftfootborder + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat1 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n")
                                    file.write(underborder * (longestlistobjectformat1 + 2 + len(leftfootborder) + len(rightfootborder)) + "\n")
                            print(Fore.GREEN + f"The table has been created at '{export}' file | {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
                    @staticmethod
                    def exporttableformat2(longestlist, longestlistobjectformat2) -> None:
                        try:
                            titled = False
                            if head != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n" + topborder * (longestlistobjectformat2 + 2 + len(leftheadborder) + len(rightheadborder)) + "\n")
                                    file.write(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder) if len(head) % 2 == 0 else file.write(leftheadborder + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2 + 1) + head + " " * int((longestlistobjectformat2 + len(leftheadborder) + len(rightheadborder)) / 2 - len(head) / 2) + rightheadborder)
                            with open(f"{export}", "a") as file:
                                file.write("\n" + topborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            for i in range(longestlist):
                                with open(f"{export}", "a") as file:
                                    file.write(f"\n{leftbodyborder} ")
                                listlong = 0
                                listnumber = 1
                                for lists in args:
                                    strlists = list(map(lambda x: nullentity if x == "" else str(x), lists))
                                    values = ExportTable.TablePatternsExport.tablepattern2export(strlists, i, longestlistobjectformat2, listlong, listnumber)
                                    listnumber = next(values)
                                    listlong = next(values)
                                if titled == False:
                                    with open(f"{export}", "a") as file:
                                        file.write("\n")
                                        file.write(middleborder * (longestlistobjectformat2 + 2 + len(lefttitleborder) + len(righttitleborder)))
                                    titled = True
                            with open(f"{export}", "a") as file:
                                file.write("\n")
                                file.write(underborder * (longestlistobjectformat2 + 2 + len(leftbodyborder) + len(rightbodyborder)))
                            if foot != None:
                                with open(f"{export}", "a") as file:
                                    file.write("\n")
                                    file.write(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n") if len(foot) % 2 == 0 else file.write(leftfootborder + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2 + 1) + foot + " " * int((longestlistobjectformat2 + len(leftfootborder) + len(rightfootborder)) / 2 - len(foot) / 2) + rightfootborder + "\n")
                                    file.write(underborder * (longestlistobjectformat2 + 2 + len(leftfootborder) + len(rightfootborder)) + "\n")
                            print(Fore.GREEN + f"The table has been created at '{export}' file | {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
                        except:
                            print(Fore.RED + "An error occured while exporting the table")
    if export == None:
        if format == 1 and title == False:
            TableFormatsNoTitle.printtableformat1(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat1(TableNeeds.findlongestlist()))
        elif format == 2 and title == False:
            TableFormatsNoTitle.printtableformat2(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat2(TableNeeds.findlongestlist()))
        elif format == 1 and title == True:
            TableFormatWithTitle.printtableformat1(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat1(TableNeeds.findlongestlist()))
        elif format == 2 and title == True:
            TableFormatWithTitle.printtableformat2(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat2(TableNeeds.findlongestlist()))
    else:
        if format == 1 and title == False:
            ExportTable.ExportTableNoTitle.exporttableformat1(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat1(TableNeeds.findlongestlist()))
        elif format == 2 and title == False:
            ExportTable.ExportTableNoTitle.exporttableformat2(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat2(TableNeeds.findlongestlist()))
        elif format == 1 and title == True:
            ExportTable.ExportTableWithTitle.exporttableformat1(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat1(TableNeeds.findlongestlist()))
        elif format == 2 and title == True:
            ExportTable.ExportTableWithTitle.exporttableformat2(TableNeeds.findlongestlist(), TableNeeds.findlongestlistobjectformat2(TableNeeds.findlongestlist()))

def onlystr(*args: str | list, remove_spaces:bool = False) -> str | list[str]:
    """
    Please use this function with 'next()' method.
    """
    for inputs in args:
        if isinstance(inputs, str):
            yield inputs.translate(str.maketrans("", "", digits)).replace(" ", "") if remove_spaces else inputs.translate(str.maketrans("", "", digits))
        elif isinstance(inputs, list):
            strlist = [x for x in list(map(lambda x: str(x).translate(str.maketrans("", "", digits)).replace(" ", "") if remove_spaces else str(x).translate(str.maketrans("", "", digits)), inputs)) if str(x) != ""]
            yield strlist

def onlyint(*args: str | list, remove_spaces:bool = False) -> int | list[int]:
    """
    Please use this function with 'next()' method.
    """
    for inputs in args:
        if isinstance(inputs, str):
            yield int(inputs.translate(str.maketrans("", "", ascii_letters)).replace(" ", "")) if remove_spaces else int(inputs.translate(str.maketrans("", "", ascii_letters)))
        if isinstance(inputs, list):
            intlist = [int(x) for x in list(map(lambda x: str(x).translate(str.maketrans("", "", ascii_letters)).replace(" ", "") if remove_spaces else str(x).translate(str.maketrans("", "", ascii_letters)), inputs)) if str(x) != ""]
            yield intlist

def strdenied(inputmassage: str, deniedmassage: str) -> int:
    print(inputmassage, end="", flush=True)
    for inputs in stdin:
        try:
            assert inputs.replace("\n", "").isdigit() == True
            break
        except AssertionError:
            stderr.write(deniedmassage)
            stderr.flush()
    return int(inputs)

def intdenied(inputmassage: str, deniedmassage: str) -> str:
    print(inputmassage, end="", flush=True)
    for inputs in stdin:
        try:
            for x in inputs.replace("\n", ""):
                assert x.isdigit() != True
            break
        except AssertionError:
            stderr.write(deniedmassage)
            stderr.flush()
    return inputs.replace("\n", "")
