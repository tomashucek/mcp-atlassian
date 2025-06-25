# MCP Atlassian Server - TODO Session 2025-06-26

## Immediate Tasks (High Priority)

### 1. Complete Jira Issue Management
- [ ] Get available transitions for DOPMO-487 (User Story)
- [ ] Transition DOPMO-487 to "Ready for UAT" status
- [ ] Add progress comment to PPM-1277 with recent accomplishments
- [ ] Test if MCP tool responses are now working properly

### 2. MCP Server Enhancements - ComAp Specific

#### Field Discovery & Validation
- [ ] Add `jira_get_project_issue_types` tool - list issue types with required fields per project
- [ ] Add `jira_get_field_schema` tool - get detailed field definitions including custom fields
- [ ] Add `jira_validate_issue_creation` tool - preview/validate issue creation before execution
- [ ] Create ComAp custom field mapping constants:
  - `customfield_12061` → Epic Name (required for Epics)
  - `customfield_15160` → Parent Link (for PPM relationships)

#### Epic Creation Helper
- [ ] Create dedicated Epic creation tool that automatically handles:
  - Epic Name requirement
  - PPM project linking
  - Proper field validation
- [ ] Add project-specific templates (DOPMO vs PPM)

### 3. User-Agent Fix Validation
- [ ] Test new Docker image `mcp-atlassian-comap:working-fixed` thoroughly
- [ ] Verify OAuth sessions work consistently with firewall
- [ ] Consider pushing fix to upstream repository

## Secondary Tasks (Medium Priority)

### 4. Docker Image Management
- [ ] Build and deploy x86 Docker image to ACR
- [ ] Tag images properly for architecture distinction
- [ ] Test multi-architecture compatibility

### 5. Error Handling Improvements
- [ ] Enhance `additional_fields` parameter validation
- [ ] Add better error messages for ComAp-specific requirements
- [ ] Document common issue creation patterns

### 6. Documentation
- [ ] Document ComAp-specific Jira field requirements
- [ ] Create examples for Epic creation with proper fields
- [ ] Update CLAUDE.md with new field discovery tools

## Issues Discovered & Fixed

### ✅ Completed Today
- **User-Agent Fix**: OAuth sessions now properly set User-Agent headers for firewall compatibility
- **DOPMO-486**: Created task "MCP Server ARM64 Docker Image Deployment"
- **DOPMO-487**: Created user story "Deploy MCP Server for Multi-Client AI Access"
- **Commit**: `a58f5a1` - User-Agent fix pushed to feature branch

### 🐛 Known Issues
1. **Epic Creation**: Requires `customfield_12061` (Epic Name) - not clearly documented
2. **MCP Tool Responses**: Tools execute successfully but responses not always visible in Claude Code
3. **Additional Fields Validation**: String vs object confusion in parameter passing
4. **Parent Linking**: Multiple ways to link issues, unclear which method to use when

### 🔧 Root Causes Identified
- ComAp custom fields not documented in MCP tools
- Firewall blocking resolved by User-Agent headers
- Pydantic validation expects JSON objects, not strings for `additional_fields`

## Context for Next Session
- Working Docker image: `mcp-atlassian-comap:working-fixed`
- Active branch: `feature/custom-user-agent`
- Recent commits focused on User-Agent OAuth fix
- PPM-1277 is parent project for all MCP server work
- DOPMO project used for manual testing and task creation

## Testing Notes
- MCP server logs show successful API calls even when Claude Code doesn't display responses
- Confluence tools work consistently, Jira tools now work after User-Agent fix
- Azure Container Registry: `comapiatsub7.azurecr.io/digitaloffice/mcp-atlassian:latest-arm64`