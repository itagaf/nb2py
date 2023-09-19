import json
import os
import re
import argparse


def readMarkDown(segment, wc):
    # parse markdown cells.
    # wc limits the number of words in a line in the final py file
    for seg in segment:
        sent = seg.split()
        if(len(sent) > wc):
            sent_l = int(len(sent) / wc)
            for i in range(sent_l + 1):
                l = (i + 1) * wc  
                l = l if len(sent) >= l else len(sent)
                output = "# " + " ".join(sent[(i * wc): l]) + "\n"
                yield output
        else:
            yield "# " + seg + "\n"
        
        
        
def readCode(segment):
    # parse code cell.
    # appends a new line character at the last line in the cell (overcome jupyter format)
    segment[-1] = segment[-1] + "\n"
    for seg in segment:
        yield seg
        
        
        
        
def main(_in_path : str, _out_path : str=None, _type : bool=None, _wc : int=15, _ignore : str=None):
    
    if(not _in_path.endswith(".ipynb")):
        raise Exception("input file is not jupyter-notebook\n")
    
    with open(_in_path) as file:
        jl = json.load(file)
    
    if (not _out_path):
        file_name = os.path.split(_in_path)[-1].split(".")[0] + ".py"
        _out_path = os.path.join(os.getcwd(), file_name)

    with open(_out_path, "w") as outFile:
        if (not os.path.exists(_out_path)):
            raise Exception("Could not write to file" + _out_path + "\n")
        
        if(_type):
            print("skipping markdown cells")
        
        for i, cell in enumerate(jl["cells"]):
            if(cell['cell_type'] == "markdown" and not (_type)):
                for seg in readMarkDown(cell['source'], _wc):
                    outFile.write(seg)
                outFile.write("\n")

            elif(cell['cell_type'] == "code"):
                if(_ignore):
                    if (re.findall(_ignore, "".join(cell['source']))):
                        print("ignoring cell #%d, containing keyword: %s" % (i, _ignore))
                        continue      
                
                for seg in readCode(cell['source']):
                    outFile.write(seg)
                        
                        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="application for quick conversion of jupyter-notebooks to .py files",
                                     epilog="author: itamar.g")
                                    
    parser.add_argument("in_path", help="path of input notebook file to be converted", type=str)
    parser.add_argument("-o","--out_path", help="path of ouput py file", type=str, default=None)
    parser.add_argument("-w","--word_count", help="number of words per line of markdown cells", type=int, default=15)
    parser.add_argument("-i","--ignore", help="string pattern which cells containing it will be ignored/skipped", type=str, default=None)
    parser.add_argument("-c", "--code_only", help="writes only code cells (exluceds markdown cells)", action="store_true", default=False)
    
    args = parser.parse_args()
    
    main(_in_path= args.in_path, 
         _out_path= args.out_path,
         _type= args.code_only,
         _wc= args.word_count,
         _ignore= args.ignore)
    