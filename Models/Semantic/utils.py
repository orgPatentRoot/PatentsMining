#import datetime


def export_dico_csv(dico,filename,delimiter):
    outfile=open(filename,'w')
    for k in dico.keys():
        outfile.write(str(k)+delimiter)
        outfile.write(str(dico[k])+'\n')


def export_matrix_csv(matrix,rownames,filename,delimiter):
    outfile=open(filename,'w')
    for i in range(len(matrix)):
        outfile.write(rownames[i]+delimiter)
        for j in range(len(matrix[i])-1):
            outfile.write(str(matrix[i][j])+delimiter)
        outfile.write(str(matrix[i][len(matrix[i])-1])+'\n')
