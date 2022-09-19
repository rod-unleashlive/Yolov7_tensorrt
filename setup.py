import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

requirements = ['numpy==1.23.2','pycuda==2022.1','nvidia-tensorrt==8.4.3.1']
# 'pytools==2022.1.12', 'opencv-python==4.5.1.48'

# setuptools.setup(
#     name="yolov7_package",
#     version="0.0.5",
#     author="Maxim Volkovskiy",
#     author_email="maxwolf8852@gmail.com",
#     description="Bindings for yolov7 in one class",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/maxwolf8852/yolov7_package.git",
#     packages=setuptools.find_packages(),
#     install_requires=requirements,
#     classifiers=[
#         "Programming Language :: Python :: 3.8",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.8',
# )

setuptools.setup(
    name='yolov7_tensorrt',
    version='1.0.0',
    url='https://github.com/rod-unleashlive/Yolov7_tensorrt.git',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
)