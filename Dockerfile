# Use an official Python runtime as a parent image
FROM python:3.10-slim-bookworm

RUN python3 -m pip install numpy
