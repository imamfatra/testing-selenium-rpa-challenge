from rpa_selenium import RpaChallange
import openpyxl, time

def input_form():
    """
    This function automates the process of filling an input form using Selenium and RPA (Robotic Process Automation).
    It reads data from an Excel file ('challenge.xlsx') and fills the form fields with the corresponding values.
    The form fields include first name, last name, company name, role in company, address, email, and phone number.
    After filling the form, it submits the form and waits for 20 seconds before quitting the browser.

    Note: The function stops after filling 10 forms.

    Returns:
        None
    """
    in_form = RpaChallange()
    in_form.start()

    wb = openpyxl.load_workbook('challenge.xlsx')
    sheet = wb.active
    counter = 0
    
    for row in sheet.rows:
        data_temp = []
        for data in row:
            if data.value == None:
                continue
            value = data.value
            data_temp.append(value)

        counter +=1
        if counter == 1:
            continue
        in_form.first_name(data_temp[0])
        in_form.last_name(data_temp[1])
        in_form.company_name(data_temp[2])
        in_form.role_in_company(data_temp[3])
        in_form.address(data_temp[4])
        in_form.email(data_temp[5])
        in_form.phone_number(data_temp[6])
        # time.sleep(10)
        in_form.submit()

        if counter > 10:
            break

    time.sleep(20)
    in_form.quit()

if __name__ := "__main__":
    input_form()