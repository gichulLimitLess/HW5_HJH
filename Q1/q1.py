#Question1
import csv

def main():
    f = open('q1.csv','r',encoding='cp949')
    data = csv.reader(f, delimiter=',')
    next(data)

    #서울이 가장 더웠던 날은 언제였을까에 대한 정보를 구하기
    #max_temp = -999
    #max_date = ''

    #서울의 연평균기온, 연평균 최저 기온, 연평균 최고 기온
    year_avg_temp = 0
    year_avg_lowtemp = 0
    year_avg_hightemp = 0

    row_count = 0

    #각각의 열에 대하여 더한다
    for row in data:
        if(row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == ''):
            continue
        
        year_avg_temp += float(row[2])
        year_avg_lowtemp += float(row[3])
        year_avg_hightemp += float(row[4])

        row_count += 1
    
    year_avg_temp = round(year_avg_temp/row_count, 3)
    year_avg_lowtemp = round(year_avg_lowtemp/row_count, 3)
    year_avg_hightemp = round(year_avg_hightemp/row_count, 3)

    
    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print('Average Temperature: {0:.2f} Celcius'.format(year_avg_temp))
    print('Average Minimum Temperature: {0:.2f} Celcius'.format(year_avg_lowtemp))
    print('Average Maximum Temperature: {0:.2f} Celcius'.format(year_avg_hightemp))

    f.close()

if __name__ == '__main__':
    main()