import Validations from "./Validations";

export default class LoginValidations {
    constructor(phone, password) {
        this.phone = phone;
        this.password = password;
    }
    checkValidaiotns() {
        let errors = [];
        if (!Validations.checkRequired(this.phone)) {
            errors['phone'] = 'The phone is required.';
        }
        if (!Validations.checkRequired(this.password)) {
            errors['password'] = 'The password is required.';
        }
        return errors;
    }
}