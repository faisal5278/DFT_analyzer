DROP TABLE IF EXISTS dft_results;

CREATE TABLE dft_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern_id TEXT NOT NULL,
    scan_chain TEXT NOT NULL,
    pass_rate REAL NOT NULL,
    test_time_ms INTEGER NOT NULL,
    timestamp TEXT NOT NULL
);
