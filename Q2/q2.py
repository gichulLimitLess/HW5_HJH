#Question1
import csv

def main():
    f = open('q2.csv','r',encoding='cp949')
    data = csv.reader(f, delimiter=',')
    next(data)

    #연평균 최저 기온, 연평균 최고 기온
    max = -100000
    min = 100000
    max_day = ""
    min_day = ""

    #각각의 열에 대하여 더한다
    for row in data:
        if(row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == ''):
            continue
        
        if max < float(row[4]) - float(row[3]):
            max = float(row[4]) - float(row[3])
            max_day = row[0]
        if min > float(row[4]) - float(row[3]):
            min = float(row[4]) - float(row[3])
            min_day = row[0]

    
    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print('Day with the Largest Temperature Variation: {0:s}'.format(max_day))
    print('Average Minimum Temperature: {0:.1f} Celcius'.format(max))
    print('Day with the Smallest Temperature Variation: {0:s}'.format(min_day))
    print('Average Minimum Temperature: {0:.1f} Celcius'.format(min))

    f.close()

if __name__ == '__main__':
    main()