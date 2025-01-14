
# Setup Instructions

Follow the steps below to set up the environment and run the scripts for this project.

## Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/prayash100/w_seg
cd w_seg
```

## Step 2: Create a Virtual Environment
Create a virtual environment in the project directory:

```bash
python -m venv venv
```

## Step 3: Activate the Virtual Environment
Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

## Step 4: Install Required Packages
Install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Step 5: Run the Scripts
Run the scripts in the following order:

1. **Download Dataset**:
   ```bash
   python download_dataset.py
   ```

2. **Split Annotations**:
   ```bash
   python split_anotation.py
   ```

3. **Split Images**:
   ```bash
   python split_images.py
   ```

After running these steps, the environment will be set up and the scripts will execute in the required order.
