# -*- coding: cp1251 -*
import numpy as np
from main_choise_window import SAPR


def create_matrix_a(number_of_knots: int, list_length: list, list_width: list, list_young_modulus: list,
                    value_left_sealing: bool, value_right_sealing: bool):

    matrix_a = np.zeros((number_of_knots, number_of_knots))

    for index in range(0, number_of_knots - 2):
        value_1 = list_young_modulus[index] * list_width[index] / list_length[index]
        value_2 = list_young_modulus[index + 1] * list_width[index + 1] / list_length[index + 1]
        value = value_1 + value_2
        position = index + 1
        matrix_a[position, position] = value
        matrix_a[position, position + 1] = matrix_a[position + 1, position] = - value_2

    if value_left_sealing:
        matrix_a[0, 0] = 1
        matrix_a[0, 1] = matrix_a[1, 0] = 0
    else:
        value_0_0 = list_young_modulus[0] * list_width[0] / list_length[0]
        matrix_a[0, 0] = value_0_0
        matrix_a[0, 1] = matrix_a[1, 0] = - value_0_0

    if value_right_sealing:
        matrix_a[number_of_knots - 1, number_of_knots - 1] = 1
        matrix_a[number_of_knots - 2, number_of_knots - 1] = 0
        matrix_a[number_of_knots - 1, number_of_knots - 2] = 0
    else:
        value_end_end = list_young_modulus[-1] * list_width[-1] / list_length[-1]
        matrix_a[number_of_knots - 1, number_of_knots - 1] = value_end_end
    return matrix_a  # type(matrix_a) = np.ndarray


def create_vector_b(input_number_of_knots: int, list_length: list, list_loads: list, list_of_sosr: list,
                    value_left_sealing: bool, value_right_sealing: bool):

    vector_b = np.zeros((input_number_of_knots, 1))

    for index in range(1, input_number_of_knots - 1):
        length_begin = list_length[index - 1]
        value_distributed_begin = list_loads[index - 1]
        length_end = list_length[index]
        value_distributed_end = list_loads[index]

        value_begin = length_begin * value_distributed_begin / 2
        value_end = length_end * value_distributed_end / 2
        value_concentrated = list_of_sosr[index]
        vector_b[index] = value_concentrated + value_begin + value_end

    if value_left_sealing:
        vector_b[0] = 0
    else:
        length_begin = list_length[0]
        value_load_begin = list_loads[0]
        value_power_begin = list_of_sosr[0]
        vector_b[0] = value_power_begin + value_load_begin * length_begin / 2

    if value_right_sealing:
        vector_b[input_number_of_knots - 1] = 0
    else:
        length_end = list_length[-1]
        value_load_end = list_loads[-1]
        value_power_end = list_of_sosr[-1]
        vector_b[input_number_of_knots - 1] = value_power_end + value_load_end * length_end / 2
    return vector_b  # type(vector_b) = np.ndarray


def calc_delta(input_list_of_length: list, input_list_of_square: list, input_list_of_raspr: list,
               input_list_of_modul: list, input_list_of_sosr: list,
               input_zadelka_l: bool, input_zadelka_r: bool):
    number_of_knots = len(input_list_of_sosr)
    matrix_a = create_matrix_a(number_of_knots, input_list_of_length, input_list_of_square, input_list_of_modul,
                               input_zadelka_l, input_zadelka_r)

    vector_b = create_vector_b(number_of_knots, input_list_of_length, input_list_of_raspr, input_list_of_sosr,
                               input_zadelka_l, input_zadelka_r)

    try:
        matrix_a = np.linalg.inv(matrix_a)
    except:
        np.linalg.lstsq(matrix_a, matrix_a)
    delta = np.dot(matrix_a, vector_b)
    #print("delta", delta)
    return delta  # type(delta) = np.ndarray


def nx_equation(input_list_of_length: list, input_list_of_square: list, input_list_of_raspr: list,
                input_list_of_modul: list, input_list_of_sosr: list,
                input_zadelka_l: bool, input_zadelka_r: bool,
                input_rod_number: int = None, input_value_x: float = None):

    delta = calc_delta(input_list_of_length, input_list_of_square, input_list_of_raspr,
                       input_list_of_modul, input_list_of_sosr, input_zadelka_l, input_zadelka_r)
    size_vector_delta = len(delta)


    answer_list = []
    for rod in range(size_vector_delta - 1):

        # EA/L
        value_1 = input_list_of_modul[rod] * input_list_of_square[rod] / input_list_of_length[rod]
        # (delta(i+1) - delta(i)
        value_2 = delta[rod + 1] - delta[rod]
        # q*L/2
        value_3 = input_list_of_raspr[rod] * input_list_of_length[rod] / 2

        if input_value_x is not None:
            # 1 - 2x/L
            value_4 = 1 - 2 * input_value_x / input_list_of_length[rod]

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n = value_1 * value_2 + value_3 * value_4
            value_n = round(value_n[0], 3)

            answer_list.append(value_n)

        else:
            # 1 - 2x/L, when x = 0: 1 - 0 = 1
            value_4_1 = 1

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n_begin = value_1 * value_2 + value_3 * value_4_1
            value_n_begin = round(value_n_begin[0], 3)

            # 1 - 2x/L, when x = L: 1 - 2 = -1
            value_4_2 = -1

            # EA/L * (delta(i+1) - delta(i) + q*L/2 * (1 - 2x/L)
            value_n_end = value_1 * value_2 + value_3 * value_4_2
            value_n_end = round(value_n_end[0], 3)

            answer_list.append([value_n_begin, value_n_end])

    if input_value_x is not None:
        return answer_list[input_rod_number - 1]  # type(answer_list[input_rod_number - 1]) = numpy.float64
    else:
        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


def ux_equation(input_list_of_length: list, input_list_of_square: list, input_list_of_raspr: list,
                input_list_of_modul: list, input_list_of_sosr: list,
                input_zadelka_l: bool, input_zadelka_r: bool,
                input_rod_number: int = None, input_value_x: float = None):

    delta = calc_delta(input_list_of_length, input_list_of_square, input_list_of_raspr,
                       input_list_of_modul, input_list_of_sosr, input_zadelka_l, input_zadelka_r)
    size_vector_delta = len(delta)

    answer_list = []
    for rod in range(size_vector_delta - 1):
        # delta(i+1) - delta(i)
        value_2 = delta[rod + 1] - delta[rod]
        # (q*L^2) / (2*E*A)
        value_3 = (input_list_of_raspr[rod] * (input_list_of_length[rod] ** 2)) / (
                2 * input_list_of_modul[rod] * input_list_of_square[rod])

        if input_value_x is not None:
            # x/L
            value_1 = input_value_x / input_list_of_length[rod]
            # 1 - x/L
            value_4 = 1 - input_value_x / input_list_of_length[rod]

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n = delta[rod] + value_1 * value_2 + value_3 * value_1 * value_4
            value_n = round(value_n[0], 3)

            answer_list.append(value_n)

        else:
            # x/L, when x = 0: 0/L = 0
            value_1_begin = 0
            # 1 - x/L, when x = 0: 1 - 0/L = 1
            value_4_begin = 1

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n_begin = delta[rod] + value_1_begin * value_2 + value_3 * value_1_begin * value_4_begin
            value_n_begin = round(value_n_begin[0], 3)

            # x/L, when x = L: L/L = 1
            value_1_end = 1
            # 1 - x/L, when x = L: 1 - L/L = 0
            value_4_end = 0

            # delta(i) + x/L * (delta(i+1) - delta(i)) + (q*L^2)/(2*E*A) * x/L * (1 - x/L)
            value_n_end = delta[rod] + value_1_end * value_2 + value_3 * value_1_end * value_4_end
            value_n_end = round(value_n_end[0], 3)

            answer_list.append([value_n_begin, value_n_end])

    if input_value_x is not None:
        return answer_list[input_rod_number - 1]  # type(answer_list[input_rod_number - 1]) = numpy.float64
    else:
        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


def sgx_equation(input_list_of_length: list, input_list_of_square: list, input_list_of_raspr: list,
                 input_list_of_modul: list, input_list_of_sosr: list,
                 input_zadelka_l: bool, input_zadelka_r: bool,
                 input_rod_number: int = None, input_value_x: float = None):

    if input_value_x is not None:
        nx_value = nx_equation(input_list_of_length, input_list_of_square, input_list_of_raspr,
                               input_list_of_modul, input_list_of_sosr, input_zadelka_l, input_zadelka_r,
                               input_rod_number, input_value_x)

        area_value = input_list_of_square[input_rod_number - 1]
        answer_value = nx_value / area_value
        return answer_value  # type(answer_value) = numpy.float64

    else:
        nx_list = nx_equation(input_list_of_length, input_list_of_square, input_list_of_raspr, input_list_of_modul,
                              input_list_of_sosr, input_zadelka_l, input_zadelka_r)

        answer_list = []
        for nx_index in range(len(nx_list)):  # for nx_index in range (N rods):
            nx_list_indexed = nx_list[nx_index]  # nx_list_indexed = [nx_begin_(nx_index)_rod, nx_end_(nx_index)_rod]
            width = input_list_of_square[nx_index]
            result_list = [round(value / width, 3) for value in nx_list_indexed]

            answer_list.append(result_list)

        return answer_list  # type(answer_list) = list[numpy.float64, numpy.float64,..., numpy.float64]


if __name__ == '__main__':
    nx = nx_equation(SAPR.list_of_length, SAPR.list_of_square, SAPR.list_of_raspr, SAPR.list_of_modul, SAPR.list_of_sosr, SAPR.zadelka_l,
                     SAPR.zadelka_r, SAPR.rod_number, SAPR.value_x)
    #print('nx_list:', nx)

    ux = ux_equation(SAPR.list_of_length, SAPR.list_of_square, SAPR.list_of_raspr, SAPR.list_of_modul, SAPR.list_of_sosr, SAPR.zadelka_l,
                     SAPR.zadelka_r, SAPR.rod_number, SAPR.value_x)
    #print('ux_list:', ux)

    sgx = sgx_equation(SAPR.list_of_length, SAPR.list_of_square, SAPR.list_of_raspr, SAPR.list_of_modul, SAPR.list_of_sosr, SAPR.zadelka_l,
                       SAPR.zadelka_r, SAPR.rod_number, SAPR.value_x)
    #print('sgx_list:', sgx)

    # nx = nx_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                        right_sealing, rod_number, value_x)
    # print('nx_list:', nx)
    #
    # sgx = sgx_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                  right_sealing, rod_number, value_x)
    # print('sgx_list:', sgx)
    #
    # ux = ux_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                        right_sealing, rod_number, value_x)
    # print('nx_list:', ux)

    # # values nx, ux, sgx in a certain value of x
    # nx_in_x = nx_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                       right_sealing, input_rod_number=1, input_value_x=2)
    # print('nx_value in x=2 in 1 rod :', nx_in_x)
    #
    # ux_in_x = ux_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                       right_sealing, input_rod_number=1, input_value_x=2)
    # print('ux_value in x=2 in 1 rod :', ux_in_x)
    #
    # sgx_in_x = sgx_equation(length_list, width_list, list_of_loads, list_of_young_modulus, powers, left_sealing,
    #                         right_sealing, input_rod_number=1, input_value_x=2)
    # print('sgx_value in x=2 in 1 rod :', sgx_in_x)
