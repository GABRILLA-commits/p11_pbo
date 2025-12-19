
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
    """
    Abstract class sebagai kontrak aturan validasi.
    """

    @abstractmethod
    def validate(self, data):
        """
        Melakukan validasi data mahasiswa.

        Args:
            data (dict): Data mahasiswa.

        Returns:
            str | None: Pesan error jika gagal, None jika valid.
        """
        pass


class SKSValidation(ValidationRule):
    """
    Validasi batas maksimal SKS mahasiswa.
    """

    def validate(self, data):
        """
        Memeriksa apakah SKS melebihi batas maksimum.

        Args:
            data (dict): Data mahasiswa.

        Returns:
            str | None: Pesan error atau None.
        """
        if data["sks"] > 24:
            return "Validasi gagal: SKS melebihi batas"
        return None


class PrerequisiteValidation(ValidationRule):
    """
    Validasi mata kuliah prasyarat.
    """
    def validate(self, data):
        """
        Memeriksa apakah prasyarat terpenuhi.

        Args:
            data (dict): Data mahasiswa.

        Returns:
            str | None: Pesan error atau None.
        """
        if not data["has_prerequisite"]:
            return "Validasi gagal: Prasyarat belum terpenuhi"
        return None


class IPKValidation(ValidationRule):
    """
    Manager utama untuk menjalankan seluruh aturan validasi.
    """
    def validate(self, data):
        if data["ipk"] < 2.75:
            return "Validasi gagal: IPK tidak memenuhi syarat"
        return None


class ValidatorManager:
    """
    Manager utama untuk menjalankan seluruh aturan validasi.
    """

    def __init__(self, validations):
        """
        Inisialisasi validator manager.

        Args:
            rules (list[ValidationRule]): Daftar aturan validasi.
        """
        self.validations = validations

    def validate(self, data):
        """
        Menjalankan proses validasi registrasi mahasiswa.

        Args:
            data (dict): Data mahasiswa.

        Returns:
            str: Hasil akhir validasi.
        """
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