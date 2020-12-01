import openpyxl, sys, os


def create_main_chart(user_name, training_days, training_type):
    #TODO: data to the name of the file (MM/YY)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = f'Hello {user_name}, you have to train for {training_days} a week, and it is a {training_type} training'

    wb.save(f'{user_name}/{user_name}_training_{training_type}.xlsx')



def volume_traninig(training_days, priority):
    pass


def intenisty_training(trainig_days, priority):
    pass

create_main_chart('wojtek', 4, 'hyper')

