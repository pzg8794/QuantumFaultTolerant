# ICNP Validation Review Images

These PNG files mirror the images embedded in `H-MABs_MasterDataset_VerificationHub.ipynb`.

They are generated from source plotting code, not by cropping exported images. Individual panels are rendered by mirroring each panel source plotting calls into standalone titleless figures. Panel titles are provided in notebook Markdown and the manifest, not embedded in the images.

- Image count: 71
- Manifest: `icnp_validation_image_manifest.csv`

Use the `ICNP-CODE-###` prefix to match each image to the validation notebook record.

## Reviewer navigation

- Start with the manifest to map each figure to its generation context.
- Use code-prefixed filenames to cross-reference notebook cells and validation records.
- Treat this directory as derived artifacts for review and verification.

## Regeneration guidance

- Regenerate images from plotting code when notebook logic or dataset slices change.
- Avoid manual image editing to preserve reproducibility.
- Update the manifest if filenames, counts, or figure provenance change.
