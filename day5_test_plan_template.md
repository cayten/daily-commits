# Day 5 — Test Plan Template ✍️

A lightweight, professional template to kickstart a real-world test plan.

## 1. Introduction
- **Project Name**: 
- **Document Owner**: 
- **Version / Date**: 
- **Purpose**: Briefly describe the objective of this test plan.
- **References**: Links to PRD, User Stories, API Docs, Designs.

## 2. Scope
- **In Scope**:
  - 
- **Out of Scope**:
  - 

## 3. Test Strategy
- **Test Levels**: Unit, Integration, API, UI (E2E), UAT, Regression.
- **Test Types**: Functional, Negative, Exploratory, Performance (Smoke), Security (basic), Compatibility.
- **Approach**:
  - Risk-based testing for critical flows.
  - Shift-left on API and unit tests; smoke UI on each commit.
  - Data-driven tests for boundary & edge cases.

## 4. Test Environment
- **Environments**: DEV / QA / STAGING / PROD
- **URLs / Endpoints**: 
- **Test Data**: Seed / Factory / Synthetic
- **Accounts**: Test users, roles & permissions
- **Tools**: Postman, Swagger, Selenium, TestNG/JUnit, CI (GitHub Actions/Jenkins).

## 5. Test Design & Coverage
- **Modules / Features**:
  - Feature A → happy path, boundary, negative
  - Feature B → permissions, validations
- **Traceability**: Map test cases to user stories or requirements (ID-based).

## 6. Entry & Exit Criteria
- **Entry**:
  - User stories Approved & Ready
  - Test environment stable
- **Exit**:
  - Critical defects (P0/P1) closed
  - Test coverage threshold met
  - Key stakeholders sign-off

## 7. Test Execution
- **Prioritization**: P0 blockers → P1 criticals → P2 minors
- **Defect Lifecycle**: New → In Progress → Fixed → Retest → Closed
- **Reporting**: Daily test summary + dashboard link

## 8. Risks & Mitigations
- Risk: Unstable environment → Mitigation: Smoke checks + rollback plan
- Risk: Test data flakiness → Mitigation: Isolated data reset per run

## 9. Schedule & Milestones
- **Sprint cadence**: 2 weeks
- **Milestones**: Test Design → Test Execution → Regression → UAT → Release

## 10. Roles & Responsibilities
- **QA**: Test design, execution, reporting
- **Dev**: Bug fixing, unit tests
- **PO/BA**: Acceptance criteria & sign-off

## 11. Metrics
- Pass/Fail rate, Defect density, MTTR, Automation coverage, Flake rate

---

> Tip: Keep this file as a template and create per-module test plans as needed.
