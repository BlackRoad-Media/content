# Contributing to BlackRoad-Media/content

Thank you for your interest in contributing to the BlackRoad ecosystem! 🎉

## 🚦 Traffic Light System

We use a traffic light system to manage contributions and issues. Please familiarize yourself with this system:

- **🟢 GreenLight:** Ready to proceed (approved, tested, validated)
- **🟡 YellowLight:** Needs review or has concerns
- **🔴 RedLight:** Critical issues or blockers (DO NOT MERGE)

See [BlackRoad Codex](.github/BLACKROAD_CODEX.md) for complete details.

## 🚀 Getting Started

### Prerequisites
- Git installed
- GitHub account
- Familiarity with Git workflow

### Setting Up Development Environment

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/content.git
   cd content
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/BlackRoad-Media/content.git
   ```

4. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 How to Contribute

### Reporting Issues

1. **Check existing issues** to avoid duplicates
2. **Choose the right template:**
   - 🟢 GreenLight: For validated items ready to proceed
   - 🟡 YellowLight: For concerns needing review
   - 🔴 RedLight: For critical/urgent issues
3. **Fill out all required fields** in the template
4. **Add relevant labels** to help categorize the issue

### Submitting Pull Requests

1. **Create a branch** for your changes
   ```bash
   git checkout -b feature/descriptive-name
   ```

2. **Make your changes**
   - Follow existing code style
   - Add/update tests as needed
   - Update documentation

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add descriptive commit message"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/descriptive-name
   ```

5. **Open a Pull Request**
   - Use the PR template
   - Indicate status (Green/Yellow/Red)
   - Fill out all sections
   - Link related issues

### Commit Message Guidelines

We follow conventional commits:

```
<type>: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

**Examples:**
```bash
feat: add YellowLight issue template
fix: correct RedLight workflow trigger
docs: update BLACKROAD_CODEX documentation
```

## 🎨 Code Style

- Follow existing code patterns
- Use consistent formatting
- Add comments for complex logic
- Keep functions focused and small
- Write descriptive variable names

## ✅ Testing

- Add tests for new features
- Ensure existing tests pass
- Test edge cases
- Validate against BlackRoad standards

## 📚 Documentation

- Update README for user-facing changes
- Add inline comments for complex code
- Update relevant documentation files
- Include examples where helpful

## 🔍 Code Review Process

### For Authors
1. **Self-review** your changes first
2. **Mark status clearly** (Green/Yellow/Red)
3. **Respond to feedback** promptly
4. **Update PR** as needed
5. **Resolve conversations** when addressed

### For Reviewers
1. **Review promptly** within 2 business days
2. **Be constructive** and specific
3. **Ask questions** for clarity
4. **Approve** when ready for merge
5. **Use traffic light labels** appropriately

### Review Criteria
- ✅ Code quality and readability
- ✅ Tests pass and provide coverage
- ✅ Documentation is complete
- ✅ Follows BlackRoad Codex standards
- ✅ No security vulnerabilities
- ✅ Performance is acceptable

## 🚦 Status Guidelines

### 🟢 When to use GreenLight
- All tests passing
- Code reviewed and approved
- Documentation complete
- No known issues
- Ready to merge

### 🟡 When to use YellowLight
- Needs additional review
- Has minor concerns
- Questions remain
- Partial implementation
- Technical debt noted

### 🔴 When to use RedLight
- Critical bugs present
- Security vulnerabilities
- Breaking changes
- Blocked by dependencies
- Not ready for review

## 🛡️ Security

- **Never commit secrets** or credentials
- **Report security issues** privately via GitHub Security
- **Follow secure coding practices**
- **Validate all inputs**
- **Use approved dependencies**

See [SECURITY.md](SECURITY.md) for details.

## 🤝 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- Be respectful and professional
- Welcome newcomers
- Give constructive feedback
- Focus on the best outcome for the community
- Show empathy towards others

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for full details.

## 📞 Getting Help

Need help contributing?

- 💬 [GitHub Discussions](https://github.com/orgs/BlackRoad-Media/discussions)
- 📖 [BlackRoad Codex](.github/BLACKROAD_CODEX.md)
- 🐛 [Report an Issue](https://github.com/BlackRoad-Media/content/issues/new/choose)

## 🎯 Recognition

Contributors who consistently provide quality contributions will be recognized:

- Listed in repository contributors
- Mentioned in release notes
- Potential for maintainer status
- Part of the BlackRoad community

## 📋 Checklist for Contributors

Before submitting your contribution:

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Commit messages follow conventions
- [ ] PR template filled out completely
- [ ] Traffic light status indicated
- [ ] Related issues linked

## 🙏 Thank You

Thank you for contributing to the BlackRoad ecosystem! Your contributions help make this project better for everyone.

---

<div align="center">
  <sub>Part of <a href="https://github.com/BlackRoad-Media">BlackRoad-Media</a> • BlackRoad Ecosystem</sub>
</div>
