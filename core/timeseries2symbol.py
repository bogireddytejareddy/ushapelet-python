import math
import numpy as np

def timeseries2symbol(data, N, n, alphabet_size):
    if alphabet_size > 20:
        return
    
    win_size = math.floor(N/n)
    dataLen = data.shape[0]
    pointers = np.zeros((dataLen+1, 1))
    symbolic_data = np.zeros((dataLen+1, n))
    lastPointer = 1

    for i in range(dataLen):
        sub_section = data[i, :]

        if N == n:
            PAA = sub_section
        
        else:
            if (N/n - math.floor(N/n)):
                temp = np.zeros(n, N)
                for j in range(n):
                    temp[j, :] = sub_section

                expanded_sub_section = np.reshape(temp, (1, N*n))
                PAA = [np.mean(np.reshape(expanded_sub_section, (N, n)))]
            else:
                PAA = [np.mean(np.reshape(sub_section, (win_size, n)))]
        
        current_string = map_to_string(PAA, alphabet_size)

        if (current_string == symbolic_data[lastPointer, :]): 
            lastPointer = lastPointer + 1
            symbolic_data[lastPointer, :] = current_string
            pointers[lastPointer] = i

    symbolic_data[0, :] = []
    pointer[0, :] = []
    symbolic_data[lastPointer:end, :] = []
    pointers[lastPointer:end, :]


def map_to_string(PAA, alphabet_size):
    string = np.zeros((1, len(PAA)))

    if alphabet_size == 2:
        cut_points  = [-np.inf, 0]
    elif alphabet_size == 3:
        cut_points  = [-np.inf, -0.43, 0.43]
    elif alphabet_size == 4:
        cut_points  = [-np.inf, -0.67, 0, 0.67]
    elif alphabet_size == 5:
        cut_points  = [-np.inf, -0.84, -0.25, 0.25, 0.84]
    elif alphabet_size == 6:
        cut_points  = [-np.inf, -0.97, -0.43, 0, 0.43, 0.97]
    elif alphabet_size == 7:
        cut_points  = [-np.inf, -1.07, -0.57, -0.18, 0.18, 0.57, 1.07]
    elif alphabet_size == 8:
        cut_points  = [-np.inf, -1.15, -0.67, -0.32, 0, 0.32, 0.67, 1.15]
    elif alphabet_size == 9:
        cut_points  = [-np.inf, -1.22, -0.76, -0.43, -0.14, 0.14, 0.43, 0.76, 1.22]
    elif alphabet_size == 10:
        cut_points  = [-np.inf, -1.28, -0.84, -0.52, -0.25, 0., 0.25, 0.52, 0.84, 1.28]
    elif alphabet_size == 11:
        cut_points  = [-np.inf, -1.34, -0.91, -0.6, -0.35, -0.11, 0.11, 0.35, 0.6, 0.91, 1.34]
    elif alphabet_size == 12:
        cut_points  = [-np.inf, -1.38, -0.97, -0.67, -0.43, -0.21, 0, 0.21, 0.43, 0.67, 0.97, 1.38]
    elif alphabet_size == 13:
        cut_points  = [-np.inf, -1.43, -1.02, -0.74, -0.5, -0.29, -0.1, 0.1, 0.29, 0.5, 0.74, 1.02, 1.43]
    elif alphabet_size == 14:
        cut_points  = [-np.inf, -1.47, -1.07, -0.79, -0.57, -0.37, -0.18, 0, 0.18, 0.37, 0.57, 0.79, 1.07, 1.47]
    elif alphabet_size == 15:
        cut_points  = [-np.inf, -1.5, -1.11, -0.84, -0.62, -0.43, -0.25, -0.08, 0.08, 0.25, 0.43, 0.62, 0.84, 1.11, 1.5]
    elif alphabet_size == 16:
        cut_points  = [-np.inf, -1.53, -1.15, -0.89, -0.67, -0.49, -0.32, -0.16, 0, 0.16, 0.32, 0.49, 0.67, 0.89, 1.15, 1.53]
    elif alphabet_size == 17:
        cut_points  = [-np.inf -1.56, -1.19, -0.93, -0.72, -0.54, -0.38, -0.22, -0.07, 0.07, 0.22, 0.38, 0.54, 0.72, 0.93, 1.19, 1.56]
    elif alphabet_size == 18:
        cut_points  = [-np.inf, -1.59, -1.22, -0.97, -0.76, -0.59, -0.43, -0.28, -0.14, 0, 0.14, 0.28 0.43, 0.59, 0.76, 0.97, 1.22, 1.59]
    elif alphabet_size == 19:
        cut_points  = [-np.inf, -1.62, -1.25, -1, -0.8, -0.63, -0.48, -0.34, -0.2, -0.07, 0.07, 0.2, 0.34, 0.48, 0.63, 0.8, 1, 1.25, 1.62]
    elif alphabet_size == 20:
        cut_points  = [-np.inf, -1.64, -1.28, -1.04, -0.84, -0.67, -0.52, -0.39, -0.25, -0.13, 0, 0.13, 0.25, 0.39, 0.52, 0.67, 0.84, 1.04, 1.28, 1.64]

    for i in range(len(PAA)):    
        string[i] = np.sum((cut_points <= PAA[i]), 2) 
