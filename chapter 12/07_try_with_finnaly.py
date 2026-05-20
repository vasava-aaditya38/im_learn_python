def main():
    try:
        n=int(input("Eneter the number: "))
        print(n)
        return
        
    except Exception as e:
        print(e)
        return

    finally:                # Use when we creare a function
        print("im inside in finally")

main()