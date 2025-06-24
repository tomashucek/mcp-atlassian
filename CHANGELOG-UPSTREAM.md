# Upstream Sync History

## 2025-06-24 - Sync with sooperset/mcp-atlassian

### Major Features Added
- **OAuth multi-cloud support** (#471, #482) - Support for bringing your own OAuth tokens
- **Confluence wiki markup support** (#531) - Added wiki markup and storage format support
- **Jira remote issue links** (#542) - Create links to external resources/Confluence pages
- **Lifecycle management improvements** (#514) - Signal safety and stdin monitoring
- **Jira batch operations** (#473) - Batch create versions tool

### Bug Fixes
- **Test infrastructure** (#558, #557, #513) - Resolved test failures and dependency constraints
- **Confluence PAT auth** (#549) - Aligned auth type with server expectations  
- **Docker container hanging** (#501) - Fixed hanging with agent SDKs
- **Stdio transport conflicts** (#522, #528) - Resolved lifecycle monitoring issues
- **Markdown to Jira conversion** (#538) - Fixed issue description formatting
- **Confluence pagination** (#530) - Removed 500 space limit in get_page_by_title

### New Tools
- `jira_get_all_projects` (#493) - List available Jira projects
- `jira_search_user` (#509) - Search for users with improved error handling
- `jira_batch_create_versions` (#473) - Batch create project versions
- `jira_create_version` (#472) - Create individual project versions

### Developer Experience
- **Environment variables** (#494) - Added MCP_LOGGING_STDOUT for stdout logging
- **Documentation** (#491) - Added AGENTS.md development guidelines
- **Docker improvements** (#497) - Enhanced SSE authentication debugging

### Technical Improvements
- Removed Cursor compatibility decorator (#515)
- Consolidated environment variable checking (#505)  
- Enhanced error handling architecture
- Improved OAuth authentication flow
- Better handling of localized issue types (#545)

### Commits Merged
ff4f19a to c3f7987 (39 commits total)

---

## Pre-sync State
- Branch: `feature/custom-user-agent`
- ComAp customizations: Custom User-Agent header support
- Last upstream sync: Initial fork