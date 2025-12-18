# AI Agent Instructions for Alzheimer's Disease Research Project

## Project Overview

This is a personal research repository for **Ziyuan Huang, PhD**, a Postdoctoral Associate at UMass Chan Medical School specializing in AI-driven Alzheimer's disease (AD) research. The focus is developing the **Alzheimer's Disease Analysis Model (ADAM)** — a multimodal AI reasoning system that integrates microbiome, immune, metabolomic, clinical, and neuroimaging data to advance AD research in diagnosis, prediction, and mechanistic understanding. This is research-stage work developing computational methods with potential for future clinical translation.

## Core Research Areas

### 1. ADAM Platform Development
- **ADAM-1**: First-generation AI model combining gut microbiome and clinical data with LLM-based reasoning
- **ADAM-2**: Next-generation platform expanding to oral/gut microbiomes, immune profiles, metabolomics, and peripheral biomarkers
- **Architecture**: Multi-agent system with computational, confounding, summarization, and classification agents
- **Key Technologies**: Large language models (LLMs), retrieval-augmented generation (RAG), chain-of-thought reasoning, SHAP interpretability

### 2. Microbiome Analysis
- **Oral-Gut Microbial Axis**: Investigating bacterial translocation and systemic inflammation in AD
- **Methods**: Metagenomic sequencing, Latent Dirichlet Allocation (LDA), differential abundance analysis
- **Data Source**: GAINS cohort (260+ participants: cognitively normal, MCI, AD)
- **Tools**: MetaPhlAn, Kraken, HUMAnN for taxonomic/functional profiling

### 3. Multimodal Data Integration
- **Data Types**: Neuroimaging, blood biomarkers (Aβ, p-tau, NfL), immune measures, metabolomics, microbiome, clinical variables
- **Framework**: ATN (Amyloid/Tau/Neurodegeneration) classification
- **Machine Learning**: Ensemble classifiers (Random Forest, XGBoost, LightGBM) with 30-seed resampling for reproducibility

## Repository Structure

```
melhzy/
├── Grant_Applications/
│   └── 2025/
│       ├── BrightFocus-AD-2025-GrantApplication.txt    # Fellowship proposal (ADAM-2.1, ADAM-2.2)
│       ├── NIH-R01-2025-GrantApplication.txt           # Multi-PI R01 proposal (ADAM Hub)
│       └── pdf_to_txt.py                               # PDF extraction utility
├── My_Publications/
│   ├── 2020/, 2023/                                    # Earlier work
│   └── 2025/
│       ├── abstract/                                   # AAIC 2025 presentation
│       ├── research/                                   # ADAM-1, microbiome, genetics papers
│       └── review/                                     # Graph neural networks commentary
├── README.md                                            # Personal profile
└── Resume_Edits.md                                      # CV/experience summary
```

## Development Workflows

### Grant Application Workflow
1. **PDF to Text Conversion**: Use `pdf_to_txt.py` with PyPDF2 to extract grant text for analysis
2. **Multi-Modal Proposals**: BrightFocus (individual fellowship, 2 years, $200K) vs NIH R01 (multi-PI, 5 years, $4M)
3. **Key Deliverables**: 
   - Classification accuracy (AUC ≥0.80, F1 ≥0.70)
   - Reproducibility across ≥70% of resampling runs
   - Literature concordance ≥80%, hallucination ≤5%

### Computational Environment
- **HPC Resources**: 
  - MGHPCC cluster (14,376 cores, 660TB storage)
  - Local workstations: Exxact 4U server with NVIDIA H200 GPUs (141GB HBM3e each)
  - Dell Precision, Mac Pro M2 Ultra systems for development
- **Software Stack**: Python, R, PyTorch, Hugging Face Transformers, SHAP, Docker/containers
- **LLM Framework**: Fine-tuning gpt-oss-20b using LoRA/QLoRA for AD-specific reasoning

### Data Analysis Patterns
1. **Preprocessing**: Bioinformatics pipelines for microbiome/multi-omics, covariate adjustment (age, sex, APOE, frailty, medications)
2. **Modeling**: Nested cross-validation, 30-seed resampling, SHAP for global/local interpretability
3. **Validation**: External benchmarking, sensitivity analyses, sex-as-biological-variable (SABV) testing
4. **Reproducibility**: Version control (GitHub), containerization, deterministic settings, NIH data sharing

## Key Conventions

### Scientific Rigor Standards
- **Performance Thresholds**: AUC ≥0.80, F1 ≥0.70 for AD classification
- **Reproducibility**: Results must replicate across ≥70% of 30 random seeds
- **Interpretability**: SHAP-based explanations with ≥80% literature alignment
- **Hallucination Control**: ≤5% unsupported claims in LLM outputs

### Biomedical Data Handling
- **HIPAA Compliance**: All clinical data de-identified, stored on institutional secure systems
- **IRB Protocols**: GAINS cohort approved (IRB #00004009)
- **Data Repositories**: NCBI SRA (microbiome), MetaboLights (metabolomics), NIAGADS (biomarkers)
- **Sample Processing**: UMass Center for Microbiome Research (Illumina MiSeq/NextSeq sequencing)

### Code Organization
- **Languages**: Python (ML/AI), R (statistical analysis), bash (HPC workflows)
- **ML Libraries**: scikit-learn, XGBoost, LightGBM, PyTorch, transformers
- **Bioinformatics**: QIIME2, Mothur, MetaPhlAn, Kraken, HUMAnN
- **Utilities**: pdf_to_txt.py demonstrates preference for simple, functional scripts

## Collaboration Context

### Key Collaborators
- **John P. Haran, MD PhD** (Mentor): Emergency Medicine, microbiome-gut-brain axis, clinical cohorts
- **Vanni Bucci, PhD** (Co-mentor): Computational microbiology, systems modeling, PMD co-director
- **AM Barrett, MD** (Collaborator): Neurology Chair, cognitive assessment, GAINS cohort access
- **Maria L. Vaida, PhD** (External): Deep learning, graph neural networks, multimodal integration

### Research Philosophy
- **Hypothesis-Driven AI**: Models must generate biologically interpretable, literature-grounded insights, not just black-box predictions
- **Modular Design**: ADAM components (computational, semantic, confounding agents) operate independently but synergistically
- **Translational Research**: Work is at research stage developing computational tools with potential for future clinical translation
- **Community Resource**: Long-term vision is open-source ADAM Hub for broader AD research community

## Domain-Specific Knowledge

### Alzheimer's Disease Biology
- **ATN Framework**: Classify by Amyloid (A), Tau (T), Neurodegeneration (N) biomarkers
- **Clinical Staging**: CN (CDR-SB 0-0.5), MCI (CDR-SB ≥1), AD (CDR-SB 1-18)
- **Peripheral Factors**: Gut/oral dysbiosis → systemic inflammation → neuroinflammation → cognitive decline
- **Key Species**: Faecalibacterium prausnitzii (protective), Bacteroides fragilis (pro-inflammatory)

### Machine Learning for Biomedicine
- **Ensemble Learning**: Combine Random Forest, XGBoost, LightGBM to reduce variance
- **Explainable AI**: SHAP values provide feature importance at global and patient levels
- **LLM Reasoning**: Chain-of-thought prompting + RAG for semantic alignment with PubMed literature
- **Confounding Control**: Dedicated agent adjusts for polypharmacy, frailty, comorbidities, sex differences

### Microbiome Research
- **16S vs Shotgun**: GAINS uses shotgun metagenomics for species-level resolution and functional pathways
- **Diversity Metrics**: Shannon index (richness), Simpson index (evenness), Bray-Curtis (β-diversity)
- **Topic Modeling**: LDA identifies co-occurring bacterial communities (analogous to text topics)
- **Differential Abundance**: LEfSe, DESeq2 for identifying AD-associated taxa

## Common Tasks & Patterns

### When Working with Grant Documents
- Convert PDFs using PyPDF2 (see `pdf_to_txt.py` template)
- Extract specific aims, hypotheses, methods, and benchmarks
- Cross-reference with published work in `My_Publications/`

### When Developing AI Models
- Start with ensemble classifiers for baseline performance
- Add LLM layer for reasoning/interpretation (not discovery)
- Use deterministic settings (fixed seeds, zero temperature) for development
- Validate with 30-seed resampling before claiming results

### When Analyzing Microbiome Data
- Preprocess with established pipelines (MetaPhlAn → HUMAnN)
- Control for clinical covariates (age, sex, meds, frailty)
- Report both taxonomic and functional (pathway) results
- Link findings to published AD microbiome literature

### When Writing Documentation
- Use scientific nomenclature correctly (italicize species names: *F. prausnitzii*)
- Include performance metrics (AUC, F1, p-values, confidence intervals)
- Cite reproducibility measures (seed count, variance)
- Reference IRB/data sharing compliance

## File-Specific Guidance

### pdf_to_txt.py
- Simple utility for converting grant PDFs to searchable text
- Uses PyPDF2 library for extraction
- Preserves page structure with separators
- Error handling for missing files
- **Pattern to follow**: Keep utilities modular, single-purpose, well-documented

### Grant Applications
- **BrightFocus**: Individual fellowship, hypothesis-driven, 2 specific aims
- **NIH R01**: Multi-PI collaborative, 3 aims with clinical site (Rhode Island Hospital)
- Both emphasize: reproducibility, interpretability, literature grounding, data sharing
- **Key insight**: Benchmarks are quantitative and testable (not aspirational)

### Publications
- 2025 is highly productive year (7 papers across abstracts, research, reviews)
- ADAM-1 published in IEEE Access (peer-reviewed, January 2025)
- AAIC 2025 abstract demonstrates oral-gut microbiome axis findings
- **Pattern**: Rapid translation from discovery → conference → journal publication

## What NOT to Do

- ❌ **Don't** use generic ML advice — focus on AD-specific challenges (class imbalance, missing data, covariate confounding)
- ❌ **Don't** ignore reproducibility — always report variance across seeds, not just mean performance
- ❌ **Don't** treat LLMs as oracles — validate all semantic outputs against literature
- ❌ **Don't** overlook HIPAA/IRB — all clinical data handling must follow institutional protocols
- ❌ **Don't** assume microbiome → AD causation — language should reflect correlational findings unless mechanistic validation exists

## Quick Reference

### Key Metrics
- Classification: AUC ≥0.80, F1 ≥0.70
- Reproducibility: ≥70% consistency across 30 seeds
- Interpretability: ≥80% literature concordance, ≤5% hallucination

### Key Cohorts
- GAINS: 260 participants (CN/MCI/AD), oral/gut microbiome + clinical + biomarkers
- Nursing Home: 335 samples, 102 participants (ADAM-1 training data)

### Key Technologies
- LLM: gpt-oss-20b fine-tuned with LoRA/QLoRA
- GPUs: NVIDIA H200 NVL (141GB HBM3e)
- Sequencing: Illumina MiSeq/NextSeq at UMass CMR
- Storage: MGHPCC cluster, 660TB capacity

### Key Outputs
- ADAM-1: IEEE Access (published)
- ADAM-2: In development (oral/gut/immune/metabolomic/biomarker integration)
- ADAM Hub: Planned open-source platform for AD community

---

**For detailed context**, refer to:
- [Grant_Applications/2025/BrightFocus-AD-2025-GrantApplication.txt](Grant_Applications/2025/BrightFocus-AD-2025-GrantApplication.txt) — ADAM-2 technical details
- [Grant_Applications/2025/NIH-R01-2025-GrantApplication.txt](Grant_Applications/2025/NIH-R01-2025-GrantApplication.txt) — ADAM Hub vision and multi-site implementation
- [Resume_Edits.md](Resume_Edits.md) — Full research trajectory and publication list
- [My_Publications/2025/research/](My_Publications/2025/research/) — Published methodologies (ADAM-1, microbiome, genetics)
