# Hi, I'm Minh

I'm a Computer Science and Data Science student at **Bucknell University**, graduating in **May 2027**. I build full-stack applications, AI tools, and software for research, and contribute fixes, features, tests, and documentation to open-source projects.

I'm interested in **2027 new graduate software engineering roles**, especially backend, data, and AI engineering.

[Portfolio](https://minhpham1810.github.io/) · [Resume](https://drive.google.com/file/d/11O6luTM8U11YWlVV34VMQCn2Wr9JrxqZ/view?usp=sharing) · [LinkedIn](https://www.linkedin.com/in/khoaminhpham18/) · [Email](mailto:minhpham181004@gmail.com)

## Open-source contributions

My upstream work spans geospatial computing, graphics, API standards, cloud infrastructure, and scientific tooling. Each entry links to the actual pull request.

### Merged

| Project | Contribution | PR |
| --- | --- | --- |
| **Apache Sedona** | Added support for Zstandard-compressed NetCDF4 raster data, including an HDF5 filter provider, regression fixture, and pixel-value checks. | [#3379](https://github.com/apache/sedona/pull/3379) |
| **Apache Sedona** | Documented how to deploy and use Sedona R on AWS EMR, covering bootstrap installation, Spark connections, and JAR configuration. | [#3334](https://github.com/apache/sedona/pull/3334) |
| **Apache Sedona** | Aligned polygon orientation predicates with PostGIS semantics for nested geometry collections and non-polygonal inputs; added null-handling coverage across execution engines. | [#3292](https://github.com/apache/sedona/pull/3292) |
| **Apache Sedona** | Preserved explicit no-CRS metadata for locally constructed GeoSeries and GeoDataFrames, avoiding unnecessary distributed SRID discovery. | [#3279](https://github.com/apache/sedona/pull/3279) |
| **GA4GH Tool Registry Service** | Corrected the OpenAPI bearer authentication scheme so API documentation and generated clients use native HTTP bearer authentication. | [#280](https://github.com/ga4gh/tool-registry-service-schemas/pull/280) |
| **Harbor Satellite** | Added a Go Report Card badge to make the project's Go code quality report accessible from its README. | [#328](https://github.com/container-registry/harbor-satellite/pull/328) |

### Open pull requests

| Project | Proposed contribution | PR |
| --- | --- | --- |
| **MaterialX** | Implemented node grouping that preserves internal and external connections, moved the operation into a reusable core API, and added tests plus a Shift+C editor shortcut. | [#3002](https://github.com/AcademySoftwareFoundation/MaterialX/pull/3002) |
| **ELIXIR Cloud FOCA** | Improved MongoDB environment-variable normalization, access-control startup logs, resource loading, and related tests. | [#256](https://github.com/elixir-cloud-aai/foca/pull/256) |
| **ELIXIR Cloud FOCA** | Added complete `MONGO_URI` configuration with precedence checks, access-control setup logs, and deprecation cleanup. | [#257](https://github.com/elixir-cloud-aai/foca/pull/257) |
| **FOSSASIA PSLab Python** | Added an in-memory connection handler and `ScienceLab(mock=True)` so development and initialization tests can run without physical hardware. | [#274](https://github.com/fossasia/pslab-python/pull/274) |

<details>
<summary>Closed proposals (not merged)</summary>

| Project | Proposed contribution | PR |
| --- | --- | --- |
| **Apache Sedona** | Proposed filtering a known degenerate-collision stack trace to prevent straight-skeleton operations from flooding executor logs. | [#3280](https://github.com/apache/sedona/pull/3280) |
| **Harbor Satellite** | Proposed centralizing password policy enforcement in the hashing function, with typed errors and updated handlers and tests. | [#331](https://github.com/container-registry/harbor-satellite/pull/331) |

</details>

*PR statuses checked October 1, 2026. [All authored pull requests](https://github.com/pulls?q=is%3Apr+author%3Aminhpham1810).*

## Highlighted projects

### [Freshness Tracker](https://github.com/minhpham1810/food-tracker)
**A hardware-to-mobile food-waste prototype**

Developed with a four-person team connecting a BME688 sensor, a Python freshness engine, FastAPI, and an Expo mobile app.

**🏆 SASEhack 2026:** Best First Hack award; Pitch Competition finalist recognition.

- Tracks temperature exposure, estimates remaining freshness, and supports label scanning and a local tool-calling assistant.
- Includes telemetry simulation and tests for the engine and API. This is an experimental waste-reduction prototype; its estimates have not been validated as food-safety measurements.

### [KALMUS Web](https://github.com/minhpham1810/kalmus_web)
**Film color analysis for researchers**

Built with a three-person team under a faculty mentor. The application lets students and researchers upload films, submit processing jobs to an HPC cluster, and explore color barcodes and interactive visualizations in a browser.

- My work includes the web interface, visualization interactions, live barcode previews, and side-by-side comparisons.
- The system connects chunked video uploads, SLURM processing, and shared storage with Next.js, Python, and Plotly.

### [OIRA Academic Chatbot](https://github.com/Bucknell-OIRA/OIRA-Chatbot)
**An assistant for Bucknell's course catalog and academic policies**

Built with a three-person team for Bucknell's Office of Institutional Research and Analytics, supervised by a full-time staff member.

- Contributed to document retrieval, academic planning, conversation memory, and the chat interface.
- Uses FastAPI, LangChain, ChromaDB, SQLite, and Next.js for retrieval, cited answers, and persistent conversations.

### [SpotOn](https://github.com/minhpham1810/SpotOn)
**Music discovery with an AI research agent**

Built an application that combines Spotify search with an agent that researches songs through Spotify, Genius, and live web search.

- Streams research progress and cited reports over server-sent events, with findings labeled verified, inferred, or speculative.
- Includes Spotify OAuth, token refresh, interactive song reports, and cached research results.

[Demo](https://www.youtube.com/watch?v=7eOdVOMNjco) · [Devpost](https://devpost.com/software/claudius-maximus)

### [unissh](https://github.com/minhpham1810/unissh)
**Clipboard images to remote servers**

Built a Go CLI that uploads clipboard images over SSH/SFTP without a remote daemon.

- Includes an interactive setup wizard, saved connection profiles, and a terminal profile picker.
- Separates clipboard access, configuration, SSH connections, and the terminal interface into focused modules.

### [FeelBit](https://github.com/minhpham1810/feelbit)
**Mood tracking and reflection**

Developed with a four-person Scrum team to help users record moods, identify triggers, and review journal entries.

- Combines mood history and statistics with AI-generated wellness tips.
- The original desktop application uses JavaFX, MongoDB, and the Gemini API.

## Tools I use

**Languages:** TypeScript / JavaScript, Python, Java, Go, C, C++, SQL  
**Applications:** React, Next.js, Expo / React Native, FastAPI, Node.js  
**AI and data:** LangChain, retrieval-augmented generation, tool-calling agents, ChromaDB, PostgreSQL, MongoDB  
**Infrastructure:** Git, Docker, GitHub Actions, Linux, HPC / SLURM
