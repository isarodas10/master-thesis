# Quick diagnostic to check which variables are defined
# Run this in a new cell BEFORE the failing cell

print("Checking required variables for summary cell...")
print("="*60)

required_vars = [
    'fa',
    'n_factors', 
    'behavioral_vars',
    'clustering_results',
    'n_clusters_to_test',
    'eval_df',
    'final_method',
    'df_final'
]

for var in required_vars:
    try:
        val = eval(var)
        if hasattr(val, 'shape'):
            print(f"✅ {var:25s} - Shape: {val.shape}")
        elif isinstance(val, (list, dict)):
            print(f"✅ {var:25s} - Length: {len(val)}")
        elif isinstance(val, (int, str)):
            print(f"✅ {var:25s} - Value: {val}")
        else:
            print(f"✅ {var:25s} - Type: {type(val).__name__}")
    except NameError:
        print(f"❌ {var:25s} - NOT DEFINED")

print("\nIf any variables show ❌, you need to run earlier cells first!")

