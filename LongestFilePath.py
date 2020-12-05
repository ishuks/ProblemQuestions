import unittest

class longestAbsolutePath: 

    def __init__(self,inputPath):
        self.longestpath = self.longestAbsoluteFilePath(inputPath)
        print(self.longestpath)

    def parseInputString(self,inp):
        '''
        Takes a file directory structure as input and returns a level separated array of names 

            Parameters: 
                Input file directory string with levels qualified by '\t' separator

            Returns: 
                File directory array with '\t' separator entries between filenames

            Complexity: 
                Assuming N file nodes, each of length K
                Time: O(NK) time 
                Space: O(NK) space 
        '''
        input_array = []
        subcount = 0 
        i = 0
        while(i < len(inp)):
            #If separator found add it to array 
            if(inp[i] == "\\"):
                if(inp[i+1] == 't'):
                    input_array.append("\t")
                #If a valid filename has already been started, add to array and reset 
                if(subcount != -1):
                    input_array.append(inp[subcount:i])
                    subcount = -1
                i+= 2

            else: 
                #If character found and filename not begun, begin counting a new filename
                if(subcount == -1): 
                    subcount = i
                i+= 1 

        input_array.append(inp[subcount:])
        return input_array

    def longestAbsoluteFilePath(self,filepath):
        '''
        Takes a directory structure as input and outputs longest file path length.

            Parameters: 
                String directory structure 

            Returns: 
                Integer longest file path length 

            Complexity: 
                Assuming N file nodes, each of length K
                    Time: O(NK) time 
                    Space: O(N) space 
        '''
        if(len(filepath) == 0): 
            return None 

        arr = self.parseInputString(filepath)
        arr_length = len(arr) 
        longest_path = [0] 

        def recurseParse(depth, path_length, arr_idx):

            #If we have reached the end of the array return 
            if(arr_idx >= arr_length): 
                return None, None

            #If we have found a file set the longest path to maximum
            if('.' in arr[arr_idx]): 
                longest_path[0] = max(longest_path[0],path_length + len(arr[arr_idx]))
            
            #Find the next depth of the file structure by number of t's 
            jump_idx = arr_idx + 1
            next_depth = 0  

            while(jump_idx < arr_length):
                if(arr[jump_idx] == '\t'): 
                    next_depth += 1 
                    jump_idx+= 1
                else:
                    break
            
            #If current sub-direc has children go down the tree 
            while(next_depth > depth and jump_idx!= None):
                jump_idx, next_depth = recurseParse(next_depth, path_length + len(arr[arr_idx]) + 1, jump_idx) 
                
            #If current sub-direc does not have children, return next destination found in file tree
            else: 
                return jump_idx, next_depth 
            
        recurseParse(0, 0, 0)
        return longest_path[0]


class TestLongestPath(unittest.TestCase): 

    def testEmptyString(self): 
       longest_path = longestAbsolutePath("") 
       self.assertEqual(None, longest_path.longestpath)
    
    def testMultiFileDirectory(self): 
        input = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        longest_path = longestAbsolutePath(input)
        self.assertEqual(32, longest_path.longestpath)

    def testSingleFileDirectory(self): 
        input = r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        longest_path = longestAbsolutePath(input)
        self.assertEqual(20, longest_path.longestpath)

    def testNoFilePresentDirectory(self): 
        input = r"dir\n\tsubdir1\n\tsubdir2"
        longest_path = longestAbsolutePath(input)
        self.assertEqual(0, longest_path.longestpath)

    def testUnbranchedDirectory(self): 
        input = r"dir\n\tsubdir1\n\t\tsubsubdir\n\t\t\tsubsubsubdir\n\t\t\t\tfile.ext"
        longest_path = longestAbsolutePath(input)
        self.assertEqual(43, longest_path.longestpath)

unittest.main()