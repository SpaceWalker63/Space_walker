def method_name():
    import string
    import random
    
    def main():
        print("A Code by-> Kartikeya Singh")
        print(" 1->For strong password \n 2->For moderate password \n 3->For weak password")
        n=int(input("Enter your choice->"))
        if n==1 :
            chars=string.ascii_letters + string.digits + string.punctuation
    
            size=input("\n Enter the size of password->")
            size=int(size)
            password=''.join(random.choice(chars) for _ in range(size))
            print(password)
        elif n==2 :
            chars=string.ascii_letters + string.digits 
            
            size=input("\n Enter the size of password->")
            size=int(size)
            password=''.join(random.choice(chars) for _ in range(size))
            print(password)
        else :
            chars=string.ascii_letters 
           
            size=input("\n Enter the size of password->")
            size=int(size)
            password=''.join(random.choice(chars) for _ in range(size))
            print(password)
    
    
    if __name__ == "__main__": 
        main()
    return main, random, string

main, random, string = method_name()
