from pathlib import Path

def initVarCommon():
    """
    Returns:
        var = {
            "input_dir": Path("input"),
            "db_file": Path("data") / "database.db",
            "ifsc_dataset_path": Path("data") / "IFSC.csv",
            "district_dataset": loadDistrictDataset(),
        }
    """
    var = {
        "input_dir": Path("input"),
        "db_file": Path("data") / "database.db",
        "ifsc_dataset_path": Path("data") / "IFSC.csv",
        "district_dataset": loadDistrictDataset(),
    }
    return var


# TODO: To be removed on implementing plugin system
def initVarCmd():
    """
    Returns:
        cmd = {
            "db": "database",
            "form": "forms",
            "ifsc": "ifsc",
            "excel": "spreadsheet",
            "bank": "neft",
            "final": "final",
        }
    """
    cmd = {
        "db": "database",
        "form": "forms",
        "ifsc": "ifsc",
        "excel": "spreadsheet",
        "bank": "neft",
        "final": "final",
    }
    return cmd


def loadDistrictDataset():
    district_list = [
        "Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alappuzha",
        "Kottayam", "Idukki", "Ernakulam", "Thrissur", "Palakkad",
        "Malappuram", "Kozhikode", "Wayanad", "Kannur", "Kasargod"
    ]
    return district_list
