#Question4
import csv

def main():
    f = open('q4.csv','r',encoding='utf-8')
    data = csv.reader(f, delimiter=',')
    next(data)

    #max_dic, min_dic은 호선 마다의 max, min 값을 가지고 있음
    max_dic={}
    min_dic={}
    station_max={'1호선':"",'2호선':"",'3호선':"",'4호선':""}
    station_min={'1호선':"",'2호선':"",'3호선':"",'4호선':""}
    lines = ['1호선', '2호선', '3호선', '4호선']

    #각각의 열에 대하여 더한다
    for row in data:
        if row[1] in lines:
            num = int(row[4]) + int(row[5])

            #max_dic이 비어있는 지, 차있는지 확인
            if row[1] in max_dic:
                if (num > max_dic[row[1]]):
                    max_dic[row[1]] = num
                    station_max[row[1]] = row[3]
                if (num < min_dic[row[1]]):
                    min_dic[row[1]] = num
                    station_min[row[1]] = row[3]
            else:
                max_dic[row[1]] = num
                station_max[row[1]] = row[3]
                min_dic[row[1]] = num
                station_min[row[1]] = row[3]
    
    print('*** Subway Report for Seoul on March 2023 ***')
    for i in range(1,5):
        print('Line {0:d}'.format(i))
        print('Busiest Station:{0:s} {1:d}'.format(station_max[str(i)+"호선"], max_dic[str(i)+"호선"]))
        print('Least used Station:{0:s} {1:d}'.format(station_min[str(i)+"호선"], min_dic[str(i)+"호선"]))

    f.close()

if __name__ == '__main__':
    main()