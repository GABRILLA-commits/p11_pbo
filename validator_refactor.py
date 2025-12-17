# STUDI KASUS: VALIDASI REGISTRASI MAHASISWA

class ValidatorManagerOld:
    def validate(self, sks, has_prerequisite):
        if sks > 24:
            return "Validasi gagal: SKS melebihi batas"
        elif not has_prerequisite:
            return "Validasi gagal: Prasyarat belum terpenuhi"
        else:
            return "Registrasi mahasiswa valid"



from abc import ABC, abstractmethod

class ValidationRule(ABC):
    @abstractmethod
    def validate(self, data):
        pass


class SKSValidation(ValidationRule):
    def validate(self, data):
        if data["sks"] > 24:
            return "Validasi gagal: SKS melebihi batas"
        return None


class PrerequisiteValidation(ValidationRule):
    def validate(self, data):
        if not data["has_prerequisite"]:
            return "Validasi gagal: Prasyarat belum terpenuhi"
        return None


class IPKValidation(ValidationRule):
    def validate(self, data):
        if data["ipk"] < 2.75:
            return "Validasi gagal: IPK tidak memenuhi syarat"
        return None


class ValidatorManager:
    def __init__(self, validations):
        self.validations = validations

    def validate(self, data):
        for rule in self.validations:
            result = rule.validate(data)
            if result is not None:
                return result
        return "Registrasi mahasiswa valid"



if __name__ == "__main__":

    print("=== SEBELUM REFACTORING ===")
    old_validator = ValidatorManagerOld()
    print(old_validator.validate(26, True))

    print("\n=== SESUDAH REFACTORING ===")
    data_mahasiswa = {
        "sks": 20,
        "has_prerequisite": True,
        "ipk": 3.1
    }

    validations = [
        SKSValidation(),
        PrerequisiteValidation(),
        IPKValidation()   # aturan baru (OCP)
    ]

    validator = ValidatorManager(validations)
    print(validator.validate(data_mahasiswa))