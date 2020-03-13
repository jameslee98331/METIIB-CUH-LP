import cv2 as cv


def main():
    filepath = 'sample_files//input//1.jpg'
    input_img = cv.cvtColor(cv.imread(filepath), cv.COLOR_BGR2RGB)
    

if __name__ == '__main__':
    main()
