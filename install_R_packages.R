# R Package Installation Script
# Master Thesis: Sexual Behavior Profiles & Social Network Analysis
# 
# Run this script to install all required R packages
# Usage: Rscript install_R_packages.R

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org/"))

# List of required packages
packages <- c(
  # Data manipulation
  "dplyr",
  "readr",
  "tidyverse",
  
  # Latent Class Analysis
  "poLCA",        # Polytomous Latent Class Analysis
  "depmixS4",     # Dependent Mixture Models
  "mclust",       # Model-based clustering
  
  # Visualization
  "plotly",
  "ggplot2",
  "corrplot",
  "RColorBrewer",
  "reshape2",
  "gridExtra",
  "grid",
  
  # Machine Learning
  "xgboost",      # Gradient boosting
  "caret",        # Classification and Regression Training
  "glmnet",       # LASSO and elastic-net regularization
  "Ckmeans.1d.dp" # Feature importance visualization
)

# Function to install packages if not already installed
install_if_missing <- function(package) {
  if (!require(package, character.only = TRUE, quietly = TRUE)) {
    cat(sprintf("Installing package: %s\n", package))
    install.packages(package, dependencies = TRUE)
  } else {
    cat(sprintf("Package already installed: %s\n", package))
  }
}

# Install all packages
cat("Starting R package installation...\n\n")
invisible(sapply(packages, install_if_missing))

cat("\n✓ All R packages installed successfully!\n")
cat("\nTo load packages in your R session, use:\n")
cat("  library(packageName)\n")
