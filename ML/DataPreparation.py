import os
import tarfile
from six.moves import urllib

DownloadRoot = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HousingPath = os.path.join("datasets", "housing")
DownloadRoot = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HousingPath = os.path.join("./datasets", "housing")
HousingURL = DownloadRoot + "datasets/housing/housing.tgz"

def fetch_housing_data(housingUrl = HousingURL, housingPath = HousingPath):
    if not os.path.isdir(housingPath):
        os.makedirs(housingPath)

    tgz_path = os.path.join(housingPath, "housing.tgz")
    urllib.request.urlretrieve(housingUrl, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = housingPath)
    housing_tgz.close()

fetch_housing_data()
