FROM public.ecr.aws/lambda/python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV APP_ENV prod

# Maximize compatibility and reduce image size
WORKDIR /var/task

# Copy function code and requirements
COPY . ${LAMBDA_TASK_ROOT}
COPY requiremets.txt ${LAMBDA_TASK_ROOT}

# Install dependencies (optimized for Lambda environment)
RUN pip install --no-cache-dir -r requiremets.txt

# Set the correct handler for Lambda execution
CMD ["app.lambda_handler"]
