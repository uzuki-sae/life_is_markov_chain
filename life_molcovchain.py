import cv2
import os
import numpy as np
import random
def main():
    dir="fotos"
    fotos=os.listdir(dir)
    markov_chain=markov(fotos)
    for photo in  markov_chain:
        cv2.imshow("img", photo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class markov():
    def __init__(self, fotos):
        self.status="W"
        self.fotos=fotos
    def change(self):
        dice=random.randrange(3)
        dice=dice%3
        if self.status=="W":
            if dice==0:
                self.status="C"
            elif dice==1:
                self.status="M"
            elif dice==2:
                self.status="Y"
        elif self.status=="C":
            if dice==0:
                self.status="W"
            elif dice==1:
                self.status="R"
            elif dice==2:
                self.status="G"
        elif self.status=="M":
            if dice==0:
                self.status="W"
            elif dice==1:
                self.status="B"
            elif dice==2:
                self.status="R"
        elif self.status=="Y":
            if dice==0:
                self.status="W"
            elif dice==1:
                self.status="B"
            elif dice==2:
                self.status="G"
        elif self.status=="R":
            if dice==0:
                self.status="K"
            elif dice==1:
                self.status="C"
            elif dice==2:
                self.status="M"
        elif self.status=="G":
            if dice==0:
                self.status="K"
            elif dice==1:
                self.status="C"
            elif dice==2:
                self.status="Y"
        elif self.status=="B":
            if dice==0:
                self.status="K"
            elif dice==1:
                self.status="M"
            elif dice==2:
                self.status="Y"
        elif self.status=="K":
            if dice==0:
                self.status="R"
            elif dice==1:
                self.status="G"
            elif dice==2:
                self.status="B"
        else:
            pass




    def process(self, photo):
        H, W, C = photo.shape
        max=np.full((H, W, 1), 255).astype(np.int32)
        B, G, R = np.split(photo.astype(np.int32), C, 2)
        if self.status == "R":
            B=R*2-max
            G=R*2-max
            R=R*2

        elif self.status == "G":
            B=G*2-max
            G=G*2
            R=G*2-max

        elif self.status == "B":
            B=B*2
            G=B*2-max
            R=B*2-max

        elif self.status == "C":
            B=B*2
            G=G*2
            R=B+G-max
        elif self.status == "M":
            B=B*2
            G=B+R-max
            R=R*2
        elif self.status == "Y":
            B=G+R-max
            G=G*2
            R=R*2
        elif self.status == "W":
            B=B*1
            G=G*1
            R=R*1
        else:
            pass
        
        if self.status == "K":
            photo=cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        else:

            photo=np.concatenate([B, G ,R], axis=2)
            photo=np.clip(photo, 0, 255).astype(np.uint8)
            
        return photo
    
    def __iter__(self):
        return self
    def __next__(self):
        
        foto=random.sample(self.fotos, k=1)
        foto=os.path.join("fotos/", foto[0])
        photo=cv2.imread(foto)
        #print(photo, foto)
        photo=self.process(photo)
        print(self.status)
        self.change()
        return photo    

            
if __name__=="__main__":
    main()

