def dataset():
    '''
    Asks the user to import a dataset from a Google Drive folder into a Google Colab 
    project and reads the first 5 indexes. Assigns the dataset to a global variable: df.
    '''
    # f = .csv
    f = input("Dataset: ")
    global df
    df = pd.read_csv("/content/drive/My Drive/datasets/" + f)
    return df.head()

dataset()
