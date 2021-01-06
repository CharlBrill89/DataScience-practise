import tabula
#check your environment via tabula-py,which shows Python, Java #version, Java version, and your OS environment.
tabula.environment_info()
#


pdf_path = "G:\Shared drives\Agrigate\Data Analytics and Data Science\Research\Industry specs and knowledge\Fresh-Food-Trade-SA-2020.pdf"
# read pdf as CSV
tabula.convert_into(pdf_path, "G:\Shared drives\Agrigate\Data Analytics and Data Science\Research\Industry specs and knowledge\Fresh-Food-Trade-SA-2020.csv", pages="all", output_format="csv", stream=True)
