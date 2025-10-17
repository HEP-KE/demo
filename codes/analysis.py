"""
Matter Power Spectrum computation using CLASS
"""

from classy import Class
import numpy as np
from .cosmology_models import (
    define_cosmology_models, 
    get_model_params, 
    compute_power_spectrum as compute_pk,
    base_params
)


def compute_power_spectrum(params, k_values):
    """
    Compute power spectrum for given cosmological parameters.

    Args:
        params: Dictionary of cosmological parameters
        k_values: Array of k values to compute P(k)

    Returns:
        Array of P(k) values or None if computation fails
    """
    try:
        cosmo = Class()
        cosmo.set(params)
        cosmo.compute()
        Pk = np.array([cosmo.pk(ki, 0.0) for ki in k_values])
        cosmo.struct_cleanup()
        cosmo.empty()
        return Pk
    except Exception as e:
        print(f"  Error: {e}")
        return None


def compute_all_models(k_values, models=None):
    """
    Compute power spectra for all defined models.
    
    Args:
        k_values: Array of k values in h/Mpc
        models: Optional dictionary of models. If None, uses define_cosmology_models()
    
    Returns:
        Dictionary with model names as keys and P(k) arrays as values
    """
    if models is None:
        models = define_cosmology_models()
    
    results = {}
    for model_name, params in models.items():
        print(f"Computing {model_name}...")
        Pk = compute_power_spectrum(params, k_values)
        if Pk is not None:
            results[model_name] = Pk
    
    return results


def compute_suppression_ratios(model_results, k_values, reference_model='ΛCDM'):
    """
    Compute power spectrum suppression relative to a reference model.
    
    Args:
        model_results: Dictionary with model names as keys and P(k) arrays as values
        k_values: Array of k values
        reference_model: Name of the reference model
        
    Returns:
        Dictionary with model names as keys and suppression ratios as values
    """
    if reference_model not in model_results:
        print(f"Warning: Reference model '{reference_model}' not found")
        return {}
    
    P_ref = model_results[reference_model]
    suppression = {}
    
    for model_name, Pk in model_results.items():
        if model_name != reference_model:
            suppression[model_name] = Pk / P_ref
    
    return suppression


def print_statistics(k_theory, model_results, k_obs, Pk_obs, σPk_obs):
    """Print summary statistics for all models and data."""
    print("\n" + "="*50)
    print("Power Spectrum Statistics")
    print("="*50)
    
    for model_name, Pk_model in model_results.items():
        if Pk_model is not None:
            print(f"\n{model_name}:")
            print(f"  P(k) range: [{Pk_model.min():.2e}, {Pk_model.max():.2e}]")
            
            # Find suppression at k=1 h/Mpc relative to ΛCDM if available
            if 'ΛCDM' in model_results and model_name != 'ΛCDM':
                k_idx = np.argmin(np.abs(k_theory - 1.0))
                suppression = Pk_model[k_idx] / model_results['ΛCDM'][k_idx]
                print(f"  Suppression at k=1 h/Mpc: {suppression:.3f}")
    
    if k_obs is not None:
        print(f"\nDR14 LyA forest:")
        print(f"  k range: [{k_obs.min():.2e}, {k_obs.max():.2e}]")
        print(f"  P(k) range: [{Pk_obs.min():.2e}, {Pk_obs.max():.2e}]")
        print(f"  Mean error: {σPk_obs.mean():.2e}")


def analyze_model_differences(model_results, k_values, k_points=[0.1, 1.0, 10.0]):
    """
    Analyze differences between models at specific k values.
    
    Args:
        model_results: Dictionary with model names and P(k) arrays
        k_values: Array of k values
        k_points: List of k values to analyze
    
    Returns:
        Dictionary with analysis results
    """
    analysis = {}
    
    if 'ΛCDM' not in model_results:
        print("Warning: ΛCDM reference model not found")
        return analysis
    
    P_ref = model_results['ΛCDM']
    
    for k_point in k_points:
        k_idx = np.argmin(np.abs(k_values - k_point))
        analysis[f'k={k_point}'] = {}
        
        for model_name, Pk in model_results.items():
            if model_name != 'ΛCDM':
                ratio = Pk[k_idx] / P_ref[k_idx]
                analysis[f'k={k_point}'][model_name] = {
                    'P(k)': Pk[k_idx],
                    'ratio': ratio,
                    'percent_diff': (ratio - 1) * 100
                }
    
    return analysis
