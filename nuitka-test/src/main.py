if __name__ == "__main__":

    file_path = './assets/message.txt'
    with open(file_path, 'r') as f:
        content = f.read()
    
    print(content)
