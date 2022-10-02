from meteor_data_class import meteorDataEntry


def main():
    name_label = 'NAME'
    mass_label = 'MASS (g)'
    print(f'{name_label:<24}{mass_label:<20}')

    ml_data = open('meteorite_landings_data.txt', 'r')
    line = ml_data.readline()

    data_list = {'Mass': list(), 'Year': list()}

    while line in ml_data.readline():
        line = line.strip('\n')
        line.split('\t')

        mass = data_list
        year = data_list

        if float(mass) <= 2900000:
            pass
        else:
            data_list['Mass'].append(ml_data)
        if int(year) >= 2013:
            data_list['Year'].append(data_list)
        print(ml_data)

    for data_list in ml_data['Mass']:
        print(f'{data_list.name:<24}{data_list.mass<20}')

    for data_list in ml_data['Year']:
        print(f'{data_list.year:<24}{data_list.year < 20}')

    return data_list


# *** code beings running here ***
if __name__ == '__main__':
    # call to main function defined above
    main()
