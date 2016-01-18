import numpy as np
import pandas as pd
from math import ceil
from calendar import monthrange
from datetime import datetime, date
from collections import OrderedDict


csv_location = 'E:\Code\\budget\\budget.csv'
current_date = datetime.now()


class Produto():
    def __init__(self, nome, qnt_refeicao=np.NaN, qnt_pacote=np.NaN, custo=np.NaN, unidade=np.NaN):
        self.nome = nome
        self.qnt_refeicao = qnt_refeicao
        self.qnt_pacote = qnt_pacote
        self.custo = custo
        self.unidade = unidade

    def __call__(self):
        return OrderedDict([('Produto', [self.nome.upper()]),
                            ('Quantidade R', [self.qnt_refeicao]),
                            ('Quantidade T', [self.qnt_pacote]),
                            ('Unidade', [self.unidade]),
                            ('Custo', [self.custo])
                            ])


class Budget():
    def __init__(self):
        today = date.today()
        self.dias = monthrange(today.year, today.month)[1]
        self.n_refeicoes = 2
        self.columns = ['Produto', 'Quantidade R',
                        'Quantidade T', 'Unidade', 'Custo', 'Custo mensal']
        try:
            self.df = pd.read_csv(csv_location)
        except ValueError:
            self.df = pd.DataFrame(data=produto, columns=self.columns)
            self.df.to_csv(csv_location, ignore_index=True, encoding='utf-8')

    def calculate_total(self):
        return self.df['Custo mensal'].sum()

    def add(self, produto):
        self.df = pd.DataFrame(data=produto(), columns=self.columns)
        try:
            self.df['Custo mensal'] = ceil(
                ((self.n_refeicoes * produto.qnt_refeicao) * self.dias) / produto.qnt_pacote) * produto.custo
        except ValueError:
            self.df['Custo mensal'] = produto.custo
        self.df.to_csv(
            csv_location, ignore_index=False, header=False, mode='a', encoding='utf-8')
        # self.df.append(calculate_total(), ignore_index=True)


    def __str__(self):
        final_output = ''
        for row in self.df.iterrows():
            final_output += '{}'.format(row)
        return final_output


o = Budget()
# print(o)
print(o.calculate_total())