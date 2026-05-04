rule all:
    input:
        "results/model_results.txt",
        "results/figures/correlations.png",
        "results/figures/feature_importance.png",
        "results/figures/net_rating_vs_wpct.png"

rule acquire:
    input:
        "team_stats_traditional_rs.csv",
        "team_stats_advanced_rs.csv"
    output:
        "data/raw/team_stats_traditional_rs.csv",
        "data/raw/team_stats_advanced_rs.csv",
        "data/raw/checksums.txt"
    shell: "python scripts/acquire.py"

rule profile:
    input:
        "data/raw/team_stats_traditional_rs.csv",
        "data/raw/team_stats_advanced_rs.csv"
    output: "results/profile_report.txt"
    shell: "python scripts/profile.py"

rule integrate:
    input:
        "data/raw/team_stats_traditional_rs.csv",
        "data/raw/team_stats_advanced_rs.csv"
    output: "data/processed/nba_merged.csv"
    shell: "python scripts/integrate.py"

rule clean:
    input: "data/processed/nba_merged.csv"
    output: "data/processed/nba_clean.csv"
    shell: "python scripts/clean.py"

rule analyze:
    input: "data/processed/nba_clean.csv"
    output:
        "results/model_results.txt",
        "results/figures/correlations.png",
        "results/figures/feature_importance.png",
        "results/figures/net_rating_vs_wpct.png"
    shell: "python scripts/analyze.py"
