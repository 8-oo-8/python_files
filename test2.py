def wordCheck(word):
    if word.startswith("comp") or word.startswith("comp"):
        print("Computing ftw!")
    elif word.endswith("omics"):
        print("Life science hipster!")
    elif word.endswith('y'):
        print("Au naturel!")
    else:
        print("Can't keep up!")


def canner_can(item):
    return "can you can a " + item + "as a canner can can a can?"


print(canner_can('can'))

if __name__ == '__main__':
    wordCheck("proteomics")
    wordCheck("quantum biology")
    wordCheck("computational neurolinguistics")
    wordCheck("cliodynamics")
