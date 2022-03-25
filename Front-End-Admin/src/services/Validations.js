export default class Validations {
    static checkPhone(phone) {
        if (phone) {
            return true;
        }
        return false;
    }
    static checkRequired(fieldValue) {
        if (fieldValue) {
            return true;
        }
        return false;
    }
}