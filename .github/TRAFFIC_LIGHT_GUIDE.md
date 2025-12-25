# 🚦 BlackRoad Traffic Light System - Quick Reference

## At a Glance

| Status | Icon | Meaning | Action |
|--------|------|---------|--------|
| **GreenLight** | 🟢 | Ready to proceed | ✅ Approve & Merge |
| **YellowLight** | 🟡 | Needs review/attention | ⚠️ Review carefully |
| **RedLight** | 🔴 | Critical/Blocked | 🚨 DO NOT MERGE |

---

## 🟢 GreenLight

### When to Use
- ✅ All tests passing
- ✅ Code review approved
- ✅ Documentation complete
- ✅ No known issues
- ✅ Security scan clean
- ✅ Ready for production

### Labels
- `status: greenlight`
- `ready`
- `approved`

### Example Scenarios
- Feature fully tested and approved
- Bug fix validated and ready
- Documentation update completed
- Release ready for deployment

### Next Steps
- Merge PR
- Deploy to production
- Close associated issues
- Celebrate! 🎉

---

## 🟡 YellowLight

### When to Use
- ⚠️ Needs additional review
- ⚠️ Has open questions
- ⚠️ Minor concerns exist
- ⚠️ Technical debt noted
- ⚠️ Performance concerns
- ⚠️ Partial implementation

### Labels
- `status: yellowlight`
- `needs-review`
- `caution`

### Example Scenarios
- Code works but needs optimization
- Documentation partially complete
- Edge cases not fully tested
- Design decisions need discussion
- Dependencies have known issues

### Next Steps
- Address concerns
- Get additional reviews
- Answer open questions
- Document limitations
- Plan follow-up work

---

## 🔴 RedLight

### When to Use
- 🚨 Production outage
- 🚨 Security vulnerability
- 🚨 Critical bug
- 🚨 Data loss risk
- 🚨 Complete blocker
- 🚨 Breaking changes

### Labels
- `status: redlight`
- `critical`
- `blocked`
- `urgent`

### Example Scenarios
- System down
- Security breach detected
- Data corruption
- Critical API failure
- Compliance violation

### Next Steps
- **STOP** - Do not merge
- Address critical issues
- Get emergency approval
- Document incident
- Implement hotfix

---

## 📋 Quick Decision Tree

```
Start: Do you have an issue or PR?
│
├─ Is it critical/broken/blocked?
│  └─ YES → 🔴 RedLight
│
├─ Does it have concerns/questions?
│  └─ YES → 🟡 YellowLight
│
└─ Is it ready/approved/tested?
   └─ YES → 🟢 GreenLight
```

---

## 🔄 Status Transitions

### Common Flow
```
🔴 RedLight (blocked)
  ↓ (fix critical issues)
🟡 YellowLight (review)
  ↓ (address concerns)
🟢 GreenLight (ready)
  ↓ (merge)
✅ Done
```

### Can Move Between
- 🟢 ↔️ 🟡 (new concerns found/resolved)
- 🟡 ↔️ 🔴 (severity changes)
- 🔴 → 🟡 → 🟢 (resolution path)

---

## 💡 Tips

### For Contributors
- **Be honest** about status
- **Update** status as work progresses
- **Communicate** when status changes
- **Document** reasons for status

### For Reviewers
- **Check** status before reviewing
- **Validate** status is accurate
- **Help** move to GreenLight
- **Block** if RedLight issues exist

### For Maintainers
- **Monitor** RedLight issues closely
- **Prioritize** by status
- **Celebrate** GreenLight merges
- **Support** YellowLight resolution

---

## 📞 Getting Help

- 📚 [Full Documentation](.github/BLACKROAD_CODEX.md)
- 💬 [Discussions](https://github.com/orgs/BlackRoad-Media/discussions)
- 📝 [Issue Templates](https://github.com/BlackRoad-Media/content/issues/new/choose)

---

## 🎯 Remember

> **🟢 GreenLight** = Ready  
> **🟡 YellowLight** = Review  
> **🔴 RedLight** = Stop

---

<div align="center">
  <sub>Part of <a href="https://github.com/BlackRoad-Media">BlackRoad-Media</a> • BlackRoad Ecosystem</sub>
</div>
