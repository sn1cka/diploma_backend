set -e
./manage.py loadtestdata api.Tour:10
./manage.py loadtestdata api.TourPhoto:10
./manage.py loadtestdata api.CompanyContacts:10
./manage.py loadtestdata api.Company:10
./manage.py loadtestdata api.CompanyFeed:100
./manage.py loadtestdata api.TourVariant:100
./manage.py loadtestdata api.TourVariantDetail:200
