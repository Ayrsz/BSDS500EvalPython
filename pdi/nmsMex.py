import cv2 as cv
import scipy as sci
import numpy as np

def nms(image):
    #Convolucoes
    E1 = sci.ndimage.uniform_filter(image, (1,1)) #Faz convolução com um filtro 2d triangular
    E2 = sci.ndimage.uniform_filter(image, (4,4))

    #Gradientes
    Ox, Oy = cv.Sobel(E2, -1, dx = 1, dy = 0), cv.Sobel(E2, -1, dx = 0, dy = 1)
    Oxx = cv.Sobel(Ox, -1, dx = 1, dy = 0)
    Oxy, Oyy = cv.Sobel(Ox, -1, dx = 0, dy = 1), cv.Sobel(Oy, -1, dx = 0, dy = 1)

    #Orientacoes
    angles = np.atan((Oyy*np.sign(-1*Oxy))/(Oxx+1e-6))
    angles = np.mod(angles, np.pi) #Mantem angulo entre [0, 180]

    #Aplica non_max supression
    result = edgesNmsMex(original_map = E1, orientations=angles, radius_supres= 5, multiplier = 1.04)

    return result

## REVISAR
def interpol(image, x, y):
    h, w = image.shape
    #Garantir que x e y estão dentro do range
    x = max(0, min(w - 1.001, x))
    y = max(0, min(h - 1.001, y))

    #Direcao
    x0, y0 = int(x), int(y)

    #Vizinhos na direcao do angulo
    x1 = min(x0 + 1, w - 1)
    y1 = min(y0 + 1, h - 1)
    dx, dy = x - x0, y - y0 #Normalmente vai ser 1
    dx1, dy1 = 1.0 - dx, 1.0 - dy
    #print(f"dx e dy {dx}, {dy}")
    #print(f"dx1 e dy1 {dx1}, {dy1}")
    #print(f"x0 e y0 {x0}, {y0}")
    return (
        image[y0, x0] * dx1 * dy1 +
        image[y0, x1] * dx  * dy1 +
        image[y1, x0] * dx1 * dy  +
        image[y1, x1] * dx  * dy
    )


def supressNoisy(nms_result, s):
    assert s > 0
    h, w = nms_result.shape
    #Suavizar bordas da imagem em cima e em baixo
    for i in range(s):
        for j in range(w):
            nms_result[i, j] *= i / s
            nms_result[h - i - 1, j] *= i / s


    #Suavizar bordas da imagem na esquerda e direita
    for i in range(h):
        for j in range(s):
            nms_result[i, j] *= j / s
            nms_result[i, w - j - 1] *= j / s

    return nms_result


#Implentation only for radius_nms = 1
def edgesNmsMex(original_map, orientations, radius_supres, multiplier):
    h, w = original_map.shape
    nms_result = original_map.copy()
    for i in range(h):
        for j in range(w):
            e = nms_result[i][j]
            if e == 0: # Se for 0, não faz nada
                continue
            e = e * multiplier #Usar para comparação, só vai suprimir se a bordar for maior
            cosin, sin = np.cos(orientations[i][j]), np.sin(orientations[i][j]) #Vetor direcao o^-> = (cos(orient), sin(orient))

            #print(cosin, sin)
            e1 = interpol(original_map, j +cosin, i+sin) #Comapara com o vizinho na direção
            e2 = interpol(original_map, j -cosin, i-sin) #Compara com o vizinho na direção e sentido oposto

            if e < e1 or e < e2:
                nms_result[i][j] = 0

    nms_result = supressNoisy(nms_result, radius_supres)
    return nms_result

if __name__ == "__main__":
    print("a")
    