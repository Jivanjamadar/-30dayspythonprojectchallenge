import cv2
from collections import deque

def flood_fill(image, start_point, new_color):
    rows, cols, _ = image.shape
    visited = set()
    queue = deque([start_point])

    start_color = image[start_point[1], start_point[0]]

    while queue:
        x, y = queue.popleft()
        if (0 <= x < cols and 0 <= y < rows and
                (x, y) not in visited and
                (image[y, x] == start_color).all()):
            image[y, x] = new_color
            visited.add((x, y))
            queue.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

def main():
    
    image = cv2.imread('dog.jpeg')

    
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # starting point for flood-fill operation
    start_point = (100, 100)  

    #  new color for flooded region
    new_color = (0, 255, 0)  # Green color

    # flood-fill operation
    flood_fill(image, start_point, new_color)

    # Display 
    cv2.imshow('Segmented Image', grayscale_image)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
