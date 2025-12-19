"""
Sistem Validasi Registrasi Mahasiswa (Praktikum 12).

Program ini melanjutkan hasil refactoring Praktikum 11
dengan menambahkan Logging untuk mencatat proses runtime.
"""

import logging
from abc import ABC, abstractmethod


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


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
            logging.warning("Validasi SKS gagal")
            return "Validasi gagal: SKS melebihi batas"

        logging.info("Validasi SKS berhasil")
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
            logging.warning("Validasi prasyarat gagal")
            return "Validasi gagal: Prasyarat belum terpenuhi"

        logging.info("Validasi prasyarat berhasil")
        return None


class RegistrationService:
    """
    Service utama untuk mengelola proses validasi registrasi mahasiswa.
    """

    def __init__(self, rules):
        """
        Inisialisasi service validasi.

        Args:
            rules (list[ValidationRule]): Daftar aturan validasi.
        """
        self.rules = rules

    def validate_registration(self, data):
        """
        Menjalankan seluruh aturan validasi registrasi.

        Args:
            data (dict): Data mahasiswa.

        Returns:
            str: Hasil akhir registrasi.
        """
        logging.info("Proses validasi registrasi dimulai")

        for rule in self.rules:
            result = rule.validate(data)
            if result is not None:
                logging.error("Registrasi mahasiswa ditolak")
                return result

        logging.info("Registrasi mahasiswa berhasil")
        return "Registrasi mahasiswa valid"


if __name__ == "__main__":
    data_mahasiswa = {
        "sks": 20,
        "has_prerequisite": True
    }

    rules = [
        SKSValidation(),
        PrerequisiteValidation()
    ]

    service = RegistrationService(rules)
    print(service.validate_registration(data_mahasiswa))
