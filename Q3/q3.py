#Question1
import csv

def main():
    f = open('q3.csv','r',encoding='utf-8')
    data = csv.reader(f, delimiter=',')
    next(data)
    
    line1_count = 0
    line2_count = 0
    line3_count = 0
    line4_count = 0
    line5_count = 0
    line6_count = 0
    line7_count = 0
    line8_count = 0
    line9_count = 0

    #각각의 열에 대하여 더한다
    for row in data:
        if row[1] == "1호선":
            line1_count += int(row[4])
            line1_count += int(row[5])
        elif row[1] == "2호선":
            line2_count += int(row[4])
            line2_count += int(row[5])
        elif row[1] == "3호선":
            line3_count += int(row[4])
            line3_count += int(row[5])
        elif row[1] == "4호선":
            line4_count += int(row[4])
            line4_count += int(row[5])
        elif row[1] == "5호선":
            line5_count += int(row[4])
            line5_count += int(row[5])
        elif row[1] == "6호선":
            line6_count += int(row[4])
            line6_count += int(row[5])
        elif row[1] == "7호선":
            line7_count += int(row[4])
            line7_count += int(row[5])
        elif row[1] == "8호선":
            line8_count += int(row[4])
            line8_count += int(row[5])
        elif row[1] == "9호선":
            line9_count += int(row[4])
            line9_count += int(row[5])

    a = {'Line1':line1_count, 'Line2':line2_count, 'Line3':line3_count, 'Line4': line4_count, 'Line5': line5_count, 'Line6': line6_count, 'Line7': line7_count, 'Line8': line8_count, 'Line9': line9_count}
    #리스트로 바꾼다 (오름차순 정렬)
    b = sorted(a.items(), key=lambda x: x[1])
    
    print('*** Subway Report for Seoul on March 2023 ***')
    print('1st Busiest Line: {0:s} {1:d}'.format(b[-1][0], b[-1][1]))
    print('2nd Busiest Line: {0:s} {1:d}'.format(b[-2][0], b[-2][1]))
    print('1st Least used Line: {0:s} {1:d}'.format(b[0][0], b[0][1]))
    print('2nd Least used Line: {0:s} {1:d}'.format(b[1][0], b[1][1]))

    f.close()

if __name__ == '__main__':
    main()