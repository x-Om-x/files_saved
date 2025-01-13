def finance_calculator(monthly_income:float, taxtrate:float, currency:str,expenses)->None:
  
  monthly_tax:float= monthly_income * (taxtrate/100)
  updated_monthly_income=monthly_income-expenses
  monthly_net_income:float= updated_monthly_income-monthly_tax
  yearly_tax:float= monthly_tax * 12
  yearly_salary:float= monthly_income * 12
  yearly_net_income:float= yearly_salary-yearly_tax
  updated_monthly_income=monthly_income-expenses
  
  print('--------')
  print(f'Monthly income: {currency}{monthly_income:,.2f}')
  print(f'Tax rate: {taxtrate:,.0f}%')
  print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
  print(f"Monthly net income: {currency}{monthly_net_income:,.2f}")
  print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
  print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
  print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
  print('-----------')

def main()->None:
  monthly_income:float=float(input("Enter your Monthly Salary: "))
  taxrate:float=float(input("Enter your Tax Rate (%): "))
  rent_pay=float(input("Enter your Rent Payment: "))
  gym_pay=float(input("Enter your Gym Payment: "))
  total_expenses:float= rent_pay + gym_pay
  

  finance_calculator(monthly_income, taxrate, "€",total_expenses)
if __name__=='__main__':
  main()
        

