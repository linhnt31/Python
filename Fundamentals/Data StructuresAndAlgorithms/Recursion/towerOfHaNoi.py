
#Time comlexity: 2 ^ n - 1

def towerHN(n, src, tmp, dst):
    if n == 1:
        print(f'Move disk {n} from {src} to {dst}')
        return 
    
    towerHN(n - 1, src, dst, tmp)
    print(f'Move disk {n} from {src} to {dst}')
    towerHN(n - 1, tmp, src, dst)

if __name__ == "__main__":
    n = int(input("Enter a radom number: "))
    towerHN(n, 'A', 'B', 'C')
