from test_locator.new_patient_locator import NewPatientLocator
from common.base_method import BaseMethod
class NewPatientPage(BaseMethod):
    def unit_new_patient(self,name,key_word,doctor_name):
        self.click(NewPatientLocator.new_loc)
        self.senk_keys(NewPatientLocator.name_loc,name)
        self.click_first_child_control(NewPatientLocator.birth_day_loc)
        self.senk_key(key_word)
        self.senk_key(0x0D)#按下enter按键
        self.senk_keys(NewPatientLocator.doctor_name_loc,doctor_name)
        self.click(NewPatientLocator.submit_loc)
    def query_prompt_name(self,key_word,doctor_name):
        self.click(NewPatientLocator.new_loc)
        self.click_first_child_control(NewPatientLocator.birth_day_loc)
        self.senk_key(key_word)
        self.senk_key(0x0D)  # 按下enter按键
        self.senk_keys(NewPatientLocator.doctor_name_loc, doctor_name)
        self.click(NewPatientLocator.submit_loc)
        text_control=self.get_text_control(NewPatientLocator.prompt_text_loc)
        act=self.get_control_name(text_control)
        self.close(NewPatientLocator.submit_prompt_loc)
        return act
    def query_prompt_birth(self,name,doctor_name):
        self.click(NewPatientLocator.new_loc)
        self.senk_keys(NewPatientLocator.name_loc,name)
        self.senk_keys(NewPatientLocator.doctor_name_loc, doctor_name)
        self.click(NewPatientLocator.submit_loc)
        text_control = self.get_text_control(NewPatientLocator.prompt_text_loc)
        act = self.get_control_name(text_control)
        self.close(NewPatientLocator.submit_prompt_loc)
        return act
    def query_prompt_doctor_name(self,name,key_word):
        self.click(NewPatientLocator.new_loc)
        self.senk_keys(NewPatientLocator.name_loc, name)
        self.click_first_child_control(NewPatientLocator.birth_day_loc)
        self.senk_key(key_word)
        self.senk_key(0x0D)  # 按下enter按键
        self.click(NewPatientLocator.submit_loc)
        text_control = self.get_text_control(NewPatientLocator.prompt_text_loc)
        act = self.get_control_name(text_control)
        self.close(NewPatientLocator.submit_prompt_loc)
        return act
    def query_doctor_name_clear(self,doctor_name):
        self.click(NewPatientLocator.new_loc)
        self.senk_keys(NewPatientLocator.doctor_name_loc, doctor_name)
        self.click(NewPatientLocator.clear_loc)
        text_control=self.get_edit_control(NewPatientLocator.doctor_name_loc)
        act=self.get_text_value(text_control)
        return act